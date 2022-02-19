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
    print(game_module.GAME_RULES)

    # Run game cycle
    correct_answers_count = 0
    while correct_answers_count < GAME_CYCLES:

        question, correct_answer = game_module.generate_question_and_answer()

        print(question)

        # Get user's answer
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                answer,
                correct_answer,
            ))
            print("Let's try again, {0}!".format(user_name))
            return

    print('Congratulations, {0}!'.format(user_name))
