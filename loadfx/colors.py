RESET="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"; UNDERLINE="\033[4m"; BLINK="\033[5m"; REVERSE="\033[7m"
BLACK="\033[30m"; RED="\033[31m"; GREEN="\033[32m"; YELLOW="\033[33m"; BLUE="\033[34m"; MAGENTA="\033[35m"; CYAN="\033[36m"; WHITE="\033[37m"; GRAY="\033[90m"
CLEAR_LINE="\033[2K"; HIDE_CURSOR="\033[?25l"; SHOW_CURSOR="\033[?25h"
def rgb(r,g,b): return f"\033[38;2;{int(r)};{int(g)};{int(b)}m"
