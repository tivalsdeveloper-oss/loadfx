import sys
from .text import TextFX

class Logger:
    def __init__(self,stream=None): self.stream=stream or sys.stdout
    def _write(self,label,msg,style): self.stream.write(style(f"[{label}] {msg}")+"\n"); self.stream.flush(); return self
    def info(self,msg): return self._write("INFO",msg,TextFX.cyan)
    def success(self,msg): return self._write(" OK ",msg,TextFX.green)
    def warning(self,msg): return self._write("WARN",msg,TextFX.yellow)
    def error(self,msg): return self._write("ERROR",msg,TextFX.red)
