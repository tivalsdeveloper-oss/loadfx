# loadfx 2.2

**Zero-dependency Python terminal effects and UI toolkit.**

LOADFX provides loading animations, progress bars, text effects, menus, widgets, themes, logging and terminal UI primitives without runtime dependencies.

## Install

```bash
python -m pip install loadfx
```

## Highlights

- 24+ built-in loading effects and custom frames
- 14 built-in progress-bar styles
- Single-line in-place progress by default
- Iterator, context-manager and decorator progress APIs
- Multi-progress and indeterminate progress
- File/download-style byte progress
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

## Progress bars

Progress bars redraw **one terminal line by default**. They do not print a new line for every update.

### Basic

```python
from loadfx import ProgressBar
import time

bar = ProgressBar(100, label="Downloading", show_eta=True, show_speed=True)
for i in range(101):
    bar.update(i)
    time.sleep(0.02)
```

### Different styles

```python
for style in ["classic", "dots", "blocks", "stars", "braille", "squares"]:
    bar = ProgressBar(100, style=style, label=style.title())
    for i in range(101):
        bar.update(i)
```

Available styles:

`classic`, `blocks`, `dots`, `dotline`, `small-dots`, `arrows`, `squares`, `circles`, `braille`, `pulse`, `bars`, `hash`, `equals`, `stars`.

### Step updates

```python
bar = ProgressBar(100, label="Installing")
for _ in range(20):
    install_step()
    bar.update(step=5)
```

### Context manager

```python
with ProgressBar(100, label="Building") as bar:
    for i in range(101):
        build_step()
        bar.update(i)
```

### Iterator helper

```python
from loadfx import track

for filename in track(files, label="Scanning", style="dots"):
    scan(filename)
```

### Indeterminate progress

Use this when the total is unknown:

```python
from loadfx import ProgressBar

bar = ProgressBar.indeterminate("Connecting")
bar.start()
connect_to_server()
bar.stop("Connected")
```

### Multiple bars

```python
from loadfx import MultiProgress

with MultiProgress() as progress:
    download = progress.add("Download", 100, style="dots")
    extract = progress.add("Extract", 100, style="blocks")
    install = progress.add("Install", 100, style="stars")

    for i in range(101):
        download.update(i)
        extract.update(min(i, 100))
        install.update(min(i * 2, 100))
        progress.refresh()
```

### Colors

```python
bar = ProgressBar(
    100,
    style="dots",
    foreground="cyan",
    background="black",
)
```

256-color values are also supported:

```python
bar = ProgressBar(100, foreground=51, background=235)
```

### Custom characters

```python
bar = ProgressBar(
    100,
    custom_fill="▓",
    custom_empty="░",
)
```

### Custom output format

```python
bar = ProgressBar(
    100,
    format_string="{label} [{bar}] {percent:.0f}% | {speed:.1f}/s | ETA {eta:.1f}s",
)
```

Supported fields include `label`, `bar`, `percent`, `current`, `total`, `speed`, `eta` and `elapsed`.

### Stream mode

If you intentionally want every update on its own line:

```python
bar = ProgressBar(10, mode="stream")
for i in range(11):
    bar.update(i)
```

The default is `mode="single"`.

## Loading effects

```python
from loadfx import Loader
import time

with Loader("Processing", effect="matrix"):
    time.sleep(2)

Loader("Processing", frames=["[   ]", "[=  ]", "[== ]", "[===]"]).start()
```

Built-in loading effects include `dots`, `spinner`, `line`, `arrows`, `bounce`, `pulse`, `circle`, `square`, `braille`, `clock`, `wave`, `bars`, `blocks`, `grow`, `shrink`, `orbit`, `arc`, `snake`, `ping`, `heart`, `star`, `matrix`, `scan`, and `moon`.

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
```

## License

MIT License. See the repository for the complete source and release history.
