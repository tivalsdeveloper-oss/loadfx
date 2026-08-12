import argparse
from . import __version__, FRAMES, Theme
from .text import TextFX

def main(argv=None):
    p=argparse.ArgumentParser(prog="loadfx",description="loadfx terminal toolkit")
    sub=p.add_subparsers(dest="cmd")
    sub.add_parser("version"); sub.add_parser("effects"); sub.add_parser("themes"); sub.add_parser("demo")
    args=p.parse_args(argv)
    if args.cmd=="version": print(__version__)
    elif args.cmd=="effects": print("\n".join(sorted(FRAMES)))
    elif args.cmd=="themes": print("\n".join(Theme.names()))
    elif args.cmd=="demo": print(TextFX.banner("LOADFX 2.0")); print(TextFX.rainbow("Terminal UI toolkit"))
    else: p.print_help()

if __name__=="__main__": main()
