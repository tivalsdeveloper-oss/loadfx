# loadfx 2.1

**Zero-dependency Python terminal effects and UI toolkit.**

## Install

```bash
python -m pip install loadfx
```

## Highlights

- 24+ built-in loading effects and custom frames
- Progress bars with ETA and speed
- Text colors, formatting, RGB, rainbow and gradient effects
- Typing, banners and boxes
- List, dictionary and nested menus
- Multi-select menus
- Tables, panels, trees and dashboard primitives
- Terminal forms, file browser, command palette and app shell
- Notifications and structured logging
- Built-in themes and task runner
- Typewriter, slide, fade-in and glitch animations
- Keyboard callback registry and plugin base class
- `loadfx` CLI with `doctor`
- Python 3.8+
- Zero runtime dependencies

## Quick start

```python
from loadfx import Loader, TextFX, Menu
import time

print(TextFX.rainbow("LOADFX"))
with Loader("Starting", effect="wave"):
    time.sleep(1)
choice = Menu({"Start":"start", "Settings":"settings", "Exit":"exit"}).show()
print(choice)
```

## Loading effects

```python
from loadfx import Loader
with Loader("Processing", effect="matrix"):
    time.sleep(2)

Loader("Processing", frames=["[   ]", "[=  ]", "[== ]", "[===]"]).start()
```

Effects include `dots`, `spinner`, `line`, `arrows`, `bounce`, `pulse`, `circle`, `square`, `braille`, `clock`, `wave`, `bars`, `blocks`, `grow`, `shrink`, `orbit`, `arc`, `snake`, `ping`, `heart`, `star`, `matrix`, `scan`, and `moon`.

## Progress

```python
from loadfx import ProgressBar
bar = ProgressBar(100, show_eta=True, show_speed=True)
for i in range(101):
    bar.update(i)
```

## Forms

```python
from loadfx import Form

form = Form("Create Account")
form.input("username", required=True)
form.password("password", required=True)
form.input("email", required=True)
result = form.show()
```

## App shell

```python
from loadfx import App

App("My App").header("LOADFX").main("Hello terminal").footer("Ready").run()
```

## Widgets and tools

```python
from loadfx import Table, Panel, Tree, FileBrowser, CommandPalette

Table(["Name", "Status"], [["loadfx", "Active"]], style="rounded").show()
Panel("Terminal toolkit", title="loadfx").show()
Tree("Project").add("src/loadfx").add("tests").show()
```

## Themes and animations

```python
from loadfx import Theme, Animation
Theme.use("cyberpunk")
Animation.fade_in("Welcome")
Animation.glitch("SYSTEM")
```

## CLI

```bash
loadfx version
loadfx effects
loadfx themes
loadfx demo
loadfx doctor
```

## API

`Loader`, `Spinner`, `ProgressBar`, `TextFX`, `Menu`, `MultiMenu`, `Table`, `Panel`, `Tree`, `Dashboard`, `Terminal`, `notify`, `Logger`, `Theme`, `Tasks`, `Animation`, `Form`, `FileBrowser`, `CommandPalette`, `keyboard`, `Plugin`, and `App`.

## License

MIT — Tivalsdeveloper
