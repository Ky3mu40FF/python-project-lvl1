#!/usr/bin/env python3
"""brain-calc game script."""

from .. import engine
from ..games import calc


def main():
    """brain-calc script entry point."""
    engine.run_game(calc)


if __name__ == '__main__':
    main()
