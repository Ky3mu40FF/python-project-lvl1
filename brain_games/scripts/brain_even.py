#!/usr/bin/env python3
"""brain_games - even game module."""

import random

import prompt

ANSWERS_TO_WIN = 3
NUM_GEN_BORDERS = (0, 20)


def game_step():
    """Generate question and checks user answer.

    Returns:
        boolean: Correctness of the answer
    """
    # Match between even check results and correct answers
    correct_answers = {True: 'yes', False: 'no'}

    # Get random integer value for question
    generated_number = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])

    # Ask user and get his answer
    print('Question: {0}'.format(generated_number))
    answer = prompt.string('Your answer: ')

    # Check if number is even and check user' answer
    is_number_even = generated_number % 2 == 0
    is_answer_correct = correct_answers[is_number_even] == answer

    # Print and return result of current step
    if is_answer_correct:
        print('Correct!')
        return True

    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
        answer, correct_answers[is_number_even],
    ))
    return False


def main():
    """brain_even entry point."""
    # Ask user for a name
    # and say hello
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))

    # Print rules of the game
    rules_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rules_text)

    # Run game cycle
    correct_answers_count = 0
    while correct_answers_count < ANSWERS_TO_WIN:
        if game_step():
            correct_answers_count += 1
        else:
            print("Let's try again, {0}!".format(user_name))
            return

    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
