"""LOADFX progress-bar examples for 2.2.0."""

import time
from loadfx import ProgressBar


# 1. Dots + foreground/background colors
bar = ProgressBar(
    100,
    width=40,
    style="dots",
    foreground="cyan",
    background="black",
    show_percent=True,
    show_eta=True,
    show_speed=True,
)
for i in range(101):
    bar.update(i)
    time.sleep(0.01)


# 2. Switch styles at runtime
bar = ProgressBar(100, width=30, style="blocks", foreground="green")
bar.update(25)
bar.set_style("braille").set_message("Extracting").update(60)
bar.set_colors("yellow", "blue").update(100)


# 3. Custom fill/empty characters
bar = ProgressBar(
    100,
    width=30,
    style="dots",
    custom_fill="▓",
    custom_empty="░",
    foreground=51,
    background=235,
)
for i in range(0, 101, 10):
    bar.update(i)
    time.sleep(0.05)


# 4. Increment with step=
bar = ProgressBar(10, style="arrows")
for _ in range(10):
    bar.update(step=1)
    time.sleep(0.05)
