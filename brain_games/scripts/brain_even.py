#!/usr/bin/env python3
"""brain-even game script."""

from .. import engine
from ..games import even


def main():
    """brain-even script entry point."""
    engine.run_game(even)


if __name__ == '__main__':
    main()
