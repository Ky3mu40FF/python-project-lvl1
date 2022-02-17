#!/usr/bin/env python3
"""brain-prime game script."""

from .. import engine
from ..games import prime


def main():
    """brain-prime script entry point."""
    engine.run_game(prime)


if __name__ == '__main__':
    main()
