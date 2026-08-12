import sys, time, threading
from .colors import HIDE_CURSOR, SHOW_CURSOR, CLEAR_LINE, RESET

FRAMES={
"dots":["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"],"spinner":["|","/","-","\\"],"line":["─","\\","│","/"],"arrows":["←","↖","↑","↗","→","↘","↓","↙"],"bounce":["⠁","⠂","⠄","⠂"],"pulse":["●","○","●","◌"],"circle":["◐","◓","◑","◒"],"square":["▖","▘","▝","▗"],"braille":["⠋","⠙","⠚","⠒","⠂","⠒","⠲","⠴","⠦","⠧","⠇","⠏"],"clock":["🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚","🕛"],
"wave":["▁","▂","▃","▄","▅","▆","▇","█","▇","▆","▅","▄","▃","▂"],"bars":["▏","▎","▍","▌","▋","▊","▉","█","▉","▊","▋","▌","▍","▎"],"blocks":["▖","▘","▝","▗","▄","▀","█","▀","▄"],"grow":[".","..","...","....","....."],"shrink":[".....","....","...","..","."],"orbit":["◴","◷","◶","◵"],"arc":["◜","◝","◞","◟"],"snake":["▰▱▱▱","▱▰▱▱","▱▱▰▱","▱▱▱▰"],"ping":["○","◌","◍","●","◍","◌"],"heart":["♡","♥","♡","♥"],"star":["✦","✧","✦","✧"],"matrix":["0","1","0","1","1","0"],"scan":["▏","▎","▍","▋","▊","▉","█","▉","▊","▋","▍","▎"],"moon":["◑","◒","◐","◓"]}

class Loader:
    def __init__(self,text="Loading...",effect="dots",interval=.08,color="",stream=None,hide_cursor=True):
        self.text=str(text); self.effect=effect; self.interval=float(interval); self.color=color; self.stream=stream or sys.stdout; self.hide_cursor=hide_cursor; self._stop=threading.Event(); self._thread=None
    def _frames(self):
        if self.effect in FRAMES: return FRAMES[self.effect]
        if isinstance(self.effect,(list,tuple)) and self.effect: return list(self.effect)
        raise ValueError(f"Unknown loading effect: {self.effect}")
    def _run(self):
        frames=self._frames(); i=0
        if self.hide_cursor: self.stream.write(HIDE_CURSOR)
        try:
            while not self._stop.is_set():
                msg=f"\r{self.color}{frames[i%len(frames)]} {self.text}{RESET if self.color else ''}"
                self.stream.write(CLEAR_LINE+msg); self.stream.flush(); i+=1; self._stop.wait(self.interval)
        finally:
            self.stream.write(CLEAR_LINE+"\r")
            if self.hide_cursor: self.stream.write(SHOW_CURSOR)
            self.stream.flush()
    def start(self):
        if self._thread and self._thread.is_alive(): return self
        self._stop.clear(); self._thread=threading.Thread(target=self._run,daemon=True); self._thread.start(); return self
    def stop(self,message=None):
        self._stop.set()
        if self._thread: self._thread.join()
        if message is not None: self.stream.write(str(message)+"\n"); self.stream.flush()
        return self
    def update(self,text=None):
        if text is not None: self.text=str(text)
        return self
    def __enter__(self): return self.start()
    def __exit__(self,exc_type,exc,tb): self.stop()

class Spinner(Loader): pass

class ProgressBar:
    def __init__(self,total=100,width=30,text="Progress",fill="█",empty="░",color="",stream=None,show_percent=True,show_eta=False,show_speed=False):
        if total<=0: raise ValueError("total must be greater than zero")
        self.total=total; self.width=max(1,int(width)); self.text=str(text); self.fill=fill; self.empty=empty; self.color=color; self.stream=stream or sys.stdout; self.current=0; self.show_percent=show_percent; self.show_eta=show_eta; self.show_speed=show_speed; self.started_at=None
    def update(self,value=None,step=None):
        if self.started_at is None: self.started_at=time.monotonic()
        if value is not None: self.current=value
        elif step is not None: self.current+=step
        self.current=max(0,min(self.current,self.total)); ratio=self.current/self.total; filled=int(self.width*ratio); bar=self.fill*filled+self.empty*(self.width-filled); parts=[f"{self.text} [{bar}]"]
        if self.show_percent: parts.append(f"{ratio*100:6.2f}%")
        elapsed=time.monotonic()-self.started_at
        if self.show_speed and elapsed>0: parts.append(f"{self.current/elapsed:.2f}/s")
        if self.show_eta and self.current>0 and elapsed>0: parts.append(f"ETA {max(0,(self.total-self.current)/(self.current/elapsed)):.1f}s")
        self.stream.write(f"\r{CLEAR_LINE}{self.color}{' '.join(parts)}{RESET if self.color else ''}"); self.stream.flush()
        if self.current>=self.total: self.stream.write("\n")
        return self
    def finish(self): return self.update(self.total)
