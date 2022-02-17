"""brain-gcd game module."""

import random

import prompt

NUM_GEN_BORDERS = (1, 200)


def get_game_rules() -> str:
    """Brain-gcd game rules getter.

    Returns:
        rules text (str): Text with brain-gcd game rules
    """
    return 'Find the greatest common divisor of given numbers.'


def game_step() -> bool:
    """Generate question and checks user answer.

    Returns:
        bool: Correctness of the answer
    """
    # Generating two random positive integer numbers
    num1, num2 = random.sample(
        range(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1]),
        2,
    )

    # Ask user
    print('Question: {0} {1}'.format(
        num1,
        num2,
    ))

    # Make a life a little easier
    if num1 < num2:
        num1, num2 = num2, num1

    correct_answer = 0

    # The Euclidean algorithm
    while True:
        remainder = num1 % num2
        if remainder == 0:
            correct_answer = num2
            break
        else:
            num1, num2 = num2, remainder

    # Get user's answer
    answer = prompt.string('Your answer: ')

    # Check user's answer
    # Print and return result of current step
    # Convert correct answer (calculated) to str
    # instead of using try-catch to convert user-inputed answer to int
    if answer == str(correct_answer):
        print('Correct!')
        return True

    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
        answer,
        correct_answer,
    ))
    return False
