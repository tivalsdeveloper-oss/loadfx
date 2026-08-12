"""Interactive terminal file browser."""
from pathlib import Path
from .menu import Menu

class FileBrowser:
    def __init__(self, path=".", title="Files"):
        self.path = Path(path).expanduser()
        self.title = title

    def show(self):
        current = self.path.resolve()
        while True:
            entries = sorted(current.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
            labels = [f"[DIR] {p.name}" if p.is_dir() else p.name for p in entries]
            options = {label: str(p) for label, p in zip(labels, entries)}
            options[".."] = str(current.parent)
            options["Select current directory"] = str(current)
            choice = Menu(options, title=f"{self.title}: {current}").show()
            if choice == str(current): return choice
            selected = Path(choice)
            if selected.is_dir(): current = selected
            else: return str(selected)
