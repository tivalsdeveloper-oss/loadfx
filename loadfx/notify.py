from .text import TextFX

class Notify:
    def success(self,msg): print(TextFX.green("✓ "+str(msg))); return self
    def error(self,msg): print(TextFX.red("✗ "+str(msg))); return self
    def warning(self,msg): print(TextFX.yellow("⚠ "+str(msg))); return self
    def info(self,msg): print(TextFX.cyan("ℹ "+str(msg))); return self

notify=Notify()
