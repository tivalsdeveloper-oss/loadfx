import time
from loadfx import Loader, ProgressBar, TextFX, Menu

print(TextFX.banner("LOADFX"))
print(TextFX.rainbow("Terminal effects library"))

with Loader("Starting", effect="dots"):
    time.sleep(1.5)

bar = ProgressBar(total=20, text="Loading")
for _ in range(20):
    time.sleep(0.05)
    bar.update(step=1)

choice = Menu({"Run demo":"run", "Settings":"settings", "Exit":"exit"}, title="Main Menu").show()
print(TextFX.green(f"Selected: {choice}"))
