"""Entry point for both `run64` and `run128`."""

import sys

from . import __version__


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if args and args[0] in ("-v", "--version", "version"):
        print(__version__)
        return 0
    print(f"128x64 {__version__} (placeholder release)")
    print("Real release coming soon: https://128x64.com")
    return 0


if __name__ == "__main__":
    sys.exit(main())