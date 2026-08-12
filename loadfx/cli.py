import argparse
from . import __version__, FRAMES, Theme
from .text import TextFX

def doctor():
    checks = {"version": __version__, "effects": len(FRAMES), "themes": len(Theme.names()), "status": "OK"}
    print("LOADFX DOCTOR")
    for key, value in checks.items(): print(f"{key:>10}: {value}")
    return checks

def main(argv=None):
    p=argparse.ArgumentParser(prog="loadfx",description="loadfx terminal toolkit")
    sub=p.add_subparsers(dest="cmd")
    sub.add_parser("version"); sub.add_parser("effects"); sub.add_parser("themes"); sub.add_parser("demo"); sub.add_parser("doctor")
    args=p.parse_args(argv)
    if args.cmd=="version": print(__version__)
    elif args.cmd=="effects": print("\n".join(sorted(FRAMES)))
    elif args.cmd=="themes": print("\n".join(Theme.names()))
    elif args.cmd=="doctor": doctor()
    elif args.cmd=="demo": print(TextFX.banner(f"LOADFX {__version__}")); print(TextFX.rainbow("Terminal UI toolkit"))
    else: p.print_help()

if __name__=="__main__": main()
