"""Game engine module."""

import prompt

GAME_CYCLES = 3


def run_game(game_module):
    """Game engine main function.

    Runs selected game.

    Args:
        game_module: game module from games directory
    """
    # Ask user for a name
    # and say hello
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))

    # Print rules of the game
    rules_text = game_module.get_game_rules()
    print(rules_text)

    # Run game cycle
    correct_answers_count = 0
    while correct_answers_count < GAME_CYCLES:
        if game_module.game_step():
            correct_answers_count += 1
        else:
            print("Let's try again, {0}!".format(user_name))
            return

    print('Congratulations, {0}!'.format(user_name))
