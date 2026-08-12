import os, shutil, sys
from .colors import HIDE_CURSOR, SHOW_CURSOR

class Cursor:
    @staticmethod
    def hide(stream=None):
        s=stream or sys.stdout; s.write(HIDE_CURSOR); s.flush()
    @staticmethod
    def show(stream=None):
        s=stream or sys.stdout; s.write(SHOW_CURSOR); s.flush()

class Terminal:
    @staticmethod
    def clear(): os.system("cls" if os.name=="nt" else "clear")
    @staticmethod
    def width(): return shutil.get_terminal_size((80,24)).columns
    @staticmethod
    def height(): return shutil.get_terminal_size((80,24)).lines
    @staticmethod
    def title(title): sys.stdout.write(f"\33]0;{title}\a"); sys.stdout.flush()
    @staticmethod
    def supports_color(): return bool(os.environ.get("TERM")) or os.name=="nt"
    @staticmethod
    def supports_unicode(): return (sys.stdout.encoding or "").lower().replace("-","") in {"utf8","utf16","utf32"} or os.name!="nt"
    @staticmethod
    def is_interactive(): return sys.stdout.isatty()

terminal=Terminal(); terminal.cursor=Cursor()
