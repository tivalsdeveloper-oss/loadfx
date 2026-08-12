# loadfx 2.2

**Zero-dependency Python terminal effects and UI toolkit.**

LOADFX provides loading animations, progress bars, text effects, menus, widgets, themes, logging and terminal UI primitives without runtime dependencies.

## Install

```bash
python -m pip install loadfx
```

## Highlights

- 24+ built-in loading effects and custom frames
- 12 built-in progress-bar styles
- Foreground and background colors, including 256-color values
- Progress percentage, speed and ETA reporting
- Custom progress-bar fill and empty characters
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
- `loadfx` CLI
- Python 3.8+
- Zero runtime dependencies

## Quick start

```python
from loadfx import Loader, TextFX, Menu
import time

print(TextFX.rainbow("LOADFX"))
with Loader("Starting", effect="wave"):
    time.sleep(1)
choice = Menu({"Start": "start", "Settings": "settings", "Exit": "exit"}).show()
print(choice)
```

## Loading effects

```python
from loadfx import Loader
import time

with Loader("Processing", effect="matrix"):
    time.sleep(2)

# Custom frames
Loader("Processing", frames=["[   ]", "[=  ]", "[== ]", "[===]"]).start()
```

Built-in loading effects include `dots`, `spinner`, `line`, `arrows`, `bounce`, `pulse`, `circle`, `square`, `braille`, `clock`, `wave`, `bars`, `blocks`, `grow`, `shrink`, `orbit`, `arc`, `snake`, `ping`, `heart`, `star`, `matrix`, `scan`, and `moon`.

## Progress bars

### Basic progress bar

```python
from loadfx import ProgressBar
import time

bar = ProgressBar(100, show_eta=True, show_speed=True)
for i in range(101):
    bar.update(i)
    time.sleep(0.02)
```

### Progress-bar styles

LOADFX includes these built-in styles:

| Style | Fill | Empty |
|---|---|---|
| `classic` | `█` | `░` |
| `blocks` | `█` | `░` |
| `dots` | `●` | `○` |
| `dotline` | `●` | `○` |
| `arrows` | `>` | `-` |
| `squares` | `■` | `□` |
| `circles` | `●` | `○` |
| `braille` | `⣿` | `⣀` |
| `pulse` | `●` | `·` |
| `bars` | `▰` | `▱` |
| `hash` | `#` | `-` |
| `equals` | `=` | `-` |

Example:

```python
from loadfx import ProgressBar

bar = ProgressBar(100, width=40, style="dots")
for i in range(101):
    bar.update(i)
```

### Foreground and background colors

Use named terminal colors or integer 256-color indexes:

```python
bar = ProgressBar(
    100,
    style="dots",
    foreground="cyan",
    background="black",
)
```

256-color example:

```python
bar = ProgressBar(
    100,
    style="blocks",
    foreground=51,
    background=235,
)
```

Supported named foreground/background colors include `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`, and their `bright_*` variants.

### Custom progress characters

```python
bar = ProgressBar(
    100,
    style="dots",
    custom_fill="▓",
    custom_empty="░",
)
```

### Runtime customization

```python
bar = ProgressBar(100, style="classic")

bar.set_style("braille")
bar.set_colors("green", "black")
bar.set_message("Installing")
bar.update(75)
```

`update()` also accepts `step=`, `message=`, and `progress=`. Use `finish()` to complete the bar.

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
```

## API

`Loader`, `Spinner`, `ProgressBar`, `TextFX`, `Menu`, `MultiMenu`, `Table`, `Panel`, `Tree`, `Dashboard`, `Terminal`, `notify`, `Logger`, `Theme`, `Tasks`, `Animation`, `Form`, `FileBrowser`, `CommandPalette`, `keyboard`, `Plugin`, and `App`.

## License

MIT — Tivalsdeveloper
