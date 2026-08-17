"""Advanced single-line progress utilities for loadfx."""
from __future__ import annotations
import functools, inspect, os, sys, time
from .colors import BACKGROUNDS, COLORS, RESET, bg256, color256

PROGRESS_STYLES = {
    "classic": ("█", "░"), "blocks": ("▰", "▱"), "dots": ("●", "○"),
    "dotline": ("●", "○"), "small-dots": ("•", "·"), "arrows": ("━", "─"),
    "squares": ("■", "□"), "circles": ("●", "○"), "braille": ("⣿", "⣀"),
    "pulse": ("●", "·"), "bars": ("▰", "▱"), "hash": ("#", "-"),
    "equals": ("=", "-"), "stars": ("★", "☆"),
}

def _fg(v):
    if v is None: return ""
    return color256(v) if isinstance(v, int) else COLORS.get(str(v).lower(), str(v))

def _bg(v):
    if v is None: return ""
    return bg256(v) if isinstance(v, int) else BACKGROUNDS.get(str(v).lower(), str(v))

class ProgressBar:
    """Single-line progress bar; updates in place unless mode='stream'."""
    def __init__(self, total=100, width=30, text="Progress", label=None, fill="█", empty="░", color="", stream=None,
                 show_percent=True, show_eta=False, show_speed=False, style="classic", foreground=None, background=None,
                 bg_color=None, custom_fill=None, custom_empty=None, mode="single", format_string=None, auto_finish=True):
        if total <= 0: raise ValueError("total must be greater than zero")
        self.total, self.width = total, max(1, int(width)); self.text = str(label if label is not None else text)
        self.stream = stream or sys.stdout; self.show_percent=show_percent; self.show_eta=show_eta; self.show_speed=show_speed
        self.color=color; self.foreground=foreground; self.background=bg_color if bg_color is not None else background
        self.mode=mode; self.format_string=format_string; self.auto_finish=auto_finish; self.current=0; self.started_at=None; self.finished=False
        self.fill, self.empty = fill, empty; self.set_style(style)
        if custom_fill is not None: self.fill=custom_fill
        if custom_empty is not None: self.empty=custom_empty

    @classmethod
    def indeterminate(cls, label="Working", style="dots", **kwargs): return IndeterminateProgress(label, style=style, **kwargs)
    @classmethod
    def from_file(cls, path, label="Reading", **kwargs): return FileProgress(path, label=label, **kwargs)

    def set_style(self, style):
        if isinstance(style, (tuple,list)):
            if len(style)!=2: raise ValueError("custom style must contain (fill, empty)")
            self.style=style; self.fill,self.empty=style; return self
        if style not in PROGRESS_STYLES: raise ValueError("Unknown progress style: {}. Available: {}".format(style, ", ".join(PROGRESS_STYLES)))
        self.style=style; self.fill,self.empty=PROGRESS_STYLES[style]; return self
    def set_colors(self, foreground=None, background=None): self.foreground,self.background=foreground,background; return self
    def set_message(self, text): self.text=str(text); return self

    def _render(self):
        ratio=max(0.0,min(1.0,self.current/float(self.total))); filled=int(self.width*ratio)
        bar=self.fill*filled+self.empty*(self.width-filled); elapsed=time.monotonic()-self.started_at if self.started_at else 0
        speed=self.current/elapsed if elapsed>0 else 0; eta=(self.total-self.current)/speed if speed>0 else 0
        if self.format_string:
            return self.format_string.format(label=self.text,bar=bar,percent=ratio*100,current=self.current,total=self.total,speed=speed,eta=eta,elapsed=elapsed)
        parts=[f"{self.text} [{bar}]"]
        if self.show_percent: parts.append(f"{ratio*100:6.2f}%")
        if self.show_speed and elapsed>0: parts.append(f"{speed:.2f}/s")
        if self.show_eta and self.current>0 and elapsed>0: parts.append(f"ETA {eta:.1f}s")
        return " ".join(parts)

    def update(self, value=None, step=None, message=None, progress=None):
        if self.started_at is None: self.started_at=time.monotonic()
        if message is not None: self.text=str(message)
        if progress is not None: value=progress
        if value is not None: self.current=value
        elif step is not None: self.current+=step
        self.current=max(0,min(self.current,self.total)); out=self._render(); prefix=self.color or _fg(self.foreground); bg=_bg(self.background)
        styled=f"{prefix}{bg}{out}{RESET if prefix or bg else ''}"
        if self.mode=="stream": self.stream.write(styled+"\n")
        else: self.stream.write("\r\033[2K"+styled)
        self.stream.flush()
        if self.current>=self.total and self.auto_finish and self.mode!="stream": self.stream.write("\n"); self.stream.flush(); self.finished=True
        return self
    def update_bytes(self, amount): return self.update(amount)
    def finish(self, message=None):
        if message is not None: self.text=str(message)
        self.current=self.total; return self.update(self.current)
    def __enter__(self):
        if self.started_at is None: self.started_at=time.monotonic()
        return self
    def __exit__(self, exc_type, exc, tb):
        if not self.finished and exc_type is None: self.finish()
        elif not self.finished and self.mode!="stream": self.stream.write("\n"); self.stream.flush()
        return False

class IndeterminateProgress:
    FRAMES={"dots":["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"],"line":["-","\\","|","/"],"blocks":["▖","▘","▝","▗"]}
    def __init__(self,label="Working",style="dots",stream=None,**kwargs): self.label=str(label); self.style=style; self.stream=stream or sys.stdout; self.i=0
    def start(self): return self
    def update(self,message=None):
        if message is not None: self.label=str(message)
        f=self.FRAMES.get(self.style,self.FRAMES["dots"])[self.i%len(self.FRAMES.get(self.style,self.FRAMES["dots"]))]; self.i+=1
        self.stream.write(f"\r\033[2K{f} {self.label}"); self.stream.flush(); return self
    def stop(self,message=None):
        if message is not None: self.label=str(message)
        self.stream.write(f"\r\033[2K{self.label}\n"); self.stream.flush(); return self
    def __enter__(self): return self.start()
    def __exit__(self,exc_type,exc,tb): self.stop(); return False

class MultiProgress:
    """Multiple bars in one terminal region."""
    def __init__(self,stream=None): self.stream=stream or sys.stdout; self.bars=[]; self.started=False
    def add(self,label,total=100,**kwargs):
        kwargs.update(stream=self.stream,auto_finish=False); b=ProgressBar(total,label=label,**kwargs); self.bars.append(b); return b
    def start(self):
        for b in self.bars:
            if b.started_at is None: b.started_at=time.monotonic()
        self.stream.write("\n"*len(self.bars)); self.refresh(); self.started=True; return self
    def refresh(self):
        if not self.bars: return self
        if self.started: self.stream.write(f"\033[{len(self.bars)}A")
        for b in self.bars: self.stream.write("\r\033[2K"+b._render()+"\n")
        self.stream.flush(); return self
    def __enter__(self): return self.start()
    def __exit__(self,exc_type,exc,tb): self.refresh(); return False

class FileProgress(ProgressBar):
    def __init__(self,path,label="Reading",**kwargs): self.path=os.fspath(path); super().__init__(os.path.getsize(self.path),label=label,**kwargs)

DownloadProgress=ProgressBar

def track(iterable,label="Processing",**kwargs):
    values=iterable if hasattr(iterable,"__len__") else list(iterable); total=len(values); bar=ProgressBar(total or 1,label=label,**kwargs)
    for i,item in enumerate(values,1): yield item; bar.update(i)

def progress(func=None,*,label=None,**kwargs):
    def decorate(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            result=fn(*args,**kw)
            if inspect.isgenerator(result): return track(result,label=label or fn.__name__,**kwargs)
            return result
        return wrapper
    return decorate(func) if func else decorate

__all__=["ProgressBar","MultiProgress","IndeterminateProgress","FileProgress","DownloadProgress","track","progress","PROGRESS_STYLES"]
