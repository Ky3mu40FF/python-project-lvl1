#!/usr/bin/env python3
"""brain-gcd game script."""

from .. import engine
from ..games import gcd


def main():
    """brain-gcd script entry point."""
    engine.run_game(gcd)


if __name__ == '__main__':
    main()
