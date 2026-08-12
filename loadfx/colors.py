RESET="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"; UNDERLINE="\033[4m"; BLINK="\033[5m"; REVERSE="\033[7m"
BLACK="\033[30m"; RED="\033[31m"; GREEN="\033[32m"; YELLOW="\033[33m"; BLUE="\033[34m"; MAGENTA="\033[35m"; CYAN="\033[36m"; WHITE="\033[37m"; GRAY="\033[90m"
BRIGHT_BLACK="\033[90m"; BRIGHT_RED="\033[91m"; BRIGHT_GREEN="\033[92m"; BRIGHT_YELLOW="\033[93m"; BRIGHT_BLUE="\033[94m"; BRIGHT_MAGENTA="\033[95m"; BRIGHT_CYAN="\033[96m"; BRIGHT_WHITE="\033[97m"
BG_BLACK="\033[40m"; BG_RED="\033[41m"; BG_GREEN="\033[42m"; BG_YELLOW="\033[43m"; BG_BLUE="\033[44m"; BG_MAGENTA="\033[45m"; BG_CYAN="\033[46m"; BG_WHITE="\033[47m"; BG_GRAY="\033[100m"
BG_BRIGHT_BLACK="\033[100m"; BG_BRIGHT_RED="\033[101m"; BG_BRIGHT_GREEN="\033[102m"; BG_BRIGHT_YELLOW="\033[103m"; BG_BRIGHT_BLUE="\033[104m"; BG_BRIGHT_MAGENTA="\033[105m"; BG_BRIGHT_CYAN="\033[106m"; BG_BRIGHT_WHITE="\033[107m"
CLEAR_LINE="\033[2K"; HIDE_CURSOR="\033[?25l"; SHOW_CURSOR="\033[?25h"

def rgb(r,g,b): return f"\033[38;2;{int(r)};{int(g)};{int(b)}m"
def bg_rgb(r,g,b): return f"\033[48;2;{int(r)};{int(g)};{int(b)}m"
def color256(n): return f"\033[38;5;{int(n)}m"
def bg256(n): return f"\033[48;5;{int(n)}m"

COLORS={
    "black":BLACK,"red":RED,"green":GREEN,"yellow":YELLOW,"blue":BLUE,"magenta":MAGENTA,"cyan":CYAN,"white":WHITE,"gray":GRAY,
    "bright_black":BRIGHT_BLACK,"bright_red":BRIGHT_RED,"bright_green":BRIGHT_GREEN,"bright_yellow":BRIGHT_YELLOW,"bright_blue":BRIGHT_BLUE,"bright_magenta":BRIGHT_MAGENTA,"bright_cyan":BRIGHT_CYAN,"bright_white":BRIGHT_WHITE,
}
BACKGROUNDS={
    "black":BG_BLACK,"red":BG_RED,"green":BG_GREEN,"yellow":BG_YELLOW,"blue":BG_BLUE,"magenta":BG_MAGENTA,"cyan":BG_CYAN,"white":BG_WHITE,"gray":BG_GRAY,
    "bright_black":BG_BRIGHT_BLACK,"bright_red":BG_BRIGHT_RED,"bright_green":BG_BRIGHT_GREEN,"bright_yellow":BG_BRIGHT_YELLOW,"bright_blue":BG_BRIGHT_BLUE,"bright_magenta":BG_BRIGHT_MAGENTA,"bright_cyan":BG_BRIGHT_CYAN,"bright_white":BG_BRIGHT_WHITE,
}
