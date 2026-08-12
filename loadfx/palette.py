"""Command palette widget."""
from .menu import Menu

class CommandPalette:
    def __init__(self, commands, title="Command Palette"):
        self.commands = list(commands)
        self.title = title

    def show(self):
        return Menu(self.commands, title=self.title, prompt="Command").show()
