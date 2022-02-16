#!/usr/bin/env python3
"""brain-progression game script."""

from .. import engine
from ..games import progression


def main():
    """brain-progression script entry point."""
    engine.run_game(progression)


if __name__ == '__main__':
    main()
