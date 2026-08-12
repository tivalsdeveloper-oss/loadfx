"""loadfx 2.1 - zero-dependency terminal effects and UI toolkit."""
from .loader import Loader, Spinner, ProgressBar, FRAMES
from .text import TextFX
from .menu import Menu
from .widgets import Table, Panel, Tree, MultiMenu, Dashboard
from .terminal import Terminal, terminal, Cursor
from .notify import Notify, notify
from .loggingx import Logger
from .theme import Theme
from .tasks import Tasks
from .animation import Animation
from .forms import Form
from .browser import FileBrowser
from .palette import CommandPalette
from .keyboard import keyboard, Keyboard
from .plugin import Plugin
from .app import App

__version__="2.1.0"
__all__=["Loader","Spinner","ProgressBar","FRAMES","TextFX","Menu","MultiMenu","Table","Panel","Tree","Dashboard","Terminal","terminal","Cursor","Notify","notify","Logger","Theme","Tasks","Animation","Form","FileBrowser","CommandPalette","keyboard","Keyboard","Plugin","App"]
