# loadfx 2.0

**Zero-dependency Python terminal effects and UI toolkit.**

## Install

```bash
python -m pip install loadfx
```

## Highlights

- 24+ built-in loading effects and custom frames
- Enhanced progress bars with ETA and speed
- Text colors, formatting, RGB, rainbow and gradient effects
- Typing, banners and boxes
- List, dictionary, multiple-dictionary and nested menus
- Multi-select menus
- Tables, panels, trees and live dashboard primitives
- Notifications and structured logging
- Built-in themes
- Task runner
- Terminal capability helpers and cursor control
- Typewriter, slide and glitch animations
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
choice=Menu({"Start":"start","Settings":"settings","Exit":"exit"}).show()
print(choice)
```

## Loading effects

```python
from loadfx import Loader
with Loader("Processing", effect="matrix"):
    do_work()
```

Effects include `dots`, `spinner`, `line`, `arrows`, `bounce`, `pulse`, `circle`, `square`, `braille`, `clock`, `wave`, `bars`, `blocks`, `grow`, `shrink`, `orbit`, `arc`, `snake`, `ping`, `heart`, `star`, `matrix`, `scan`, and `moon`.

Custom frames are supported:

```python
Loader("Working", effect=["◐","◓","◑","◒"]).start()
```

## Progress

```python
from loadfx import ProgressBar
bar=ProgressBar(100,show_eta=True,show_speed=True)
for i in range(101): bar.update(i)
```

## Widgets

```python
from loadfx import Table, Panel, Tree

Table(["Name","Status"], [["loadfx","Active"]], style="rounded").show()
Panel("Terminal toolkit", title="loadfx").show()
Tree("Project").add("src/loadfx").add("tests").show()
```

## Multi-select menu

```python
from loadfx import MultiMenu
selected=MultiMenu(["Python","HTML","CSS","JavaScript"]).show()
```

## Themes and notifications

```python
from loadfx import Theme, notify
Theme.use("cyberpunk")
notify.success("Build complete")
notify.warning("Development mode")
```

## CLI

```bash
loadfx version
loadfx effects
loadfx themes
loadfx demo
```

## API

`Loader`, `Spinner`, `ProgressBar`, `TextFX`, `Menu`, `MultiMenu`, `Table`, `Panel`, `Tree`, `Dashboard`, `Terminal`, `notify`, `Logger`, `Theme`, `Tasks`, and `Animation`.

## License

MIT — Tivalsdeveloper
