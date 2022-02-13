#!/usr/bin/env python3
"""brain_games main module."""

from ..cli import welcome_user


def main():
    """brain_games entry point."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
