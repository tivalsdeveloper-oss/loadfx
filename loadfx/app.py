"""Small composable terminal application shell."""
from .widgets import Panel

class App:
    def __init__(self, title="loadfx"):
        self.title = title; self._header = None; self._sidebar = None; self._main = None; self._footer = None

    def header(self, value): self._header = value; return self
    def sidebar(self, value): self._sidebar = value; return self
    def main(self, value): self._main = value; return self
    def footer(self, value): self._footer = value; return self

    def run(self):
        print(f"\n=== {self.title} ===")
        for label, value in (("HEADER", self._header), ("SIDEBAR", self._sidebar), ("MAIN", self._main), ("FOOTER", self._footer)):
            if value is not None: print(f"[{label}]\n{value}")
        return self
