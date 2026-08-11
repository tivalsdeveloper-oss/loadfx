# loadfx

A lightweight, zero-dependency Python terminal library for loading effects, progress bars, text effects, and interactive menus.

## Install

```bash
python -m pip install loadfx
```

## Quick start

```python
from loadfx import Loader, TextFX, Menu
import time

print(TextFX.rainbow("LOADFX"))

with Loader("Starting", effect="dots"):
    time.sleep(2)

choice = Menu({
    "Start": "start",
    "Settings": "settings",
    "Exit": "exit"
}).show()

print(TextFX.green(f"Selected: {choice}"))
```

## Features

- 10+ loading/spinner effects
- Progress bars
- Terminal colors and formatting
- Typing, rainbow, and gradient text
- Banners and boxes
- Menus from lists
- Menus from dictionaries
- Multiple dictionaries
- Nested menus
- Zero runtime dependencies

See `docs/index.html` for the full documentation.

## License

MIT
