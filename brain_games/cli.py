"""cli module."""

import prompt


def welcome_user():
    """Greeting function."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
