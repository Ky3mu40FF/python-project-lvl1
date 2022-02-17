"""Brain-prime game module."""

import math
import random

import prompt

MAX_RAND_VALUE = 10


def get_game_rules() -> str:
    """brain-prime game rules getter.

    Returns:
        rules text (str): Text with brain-prime game rules
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Check if given number is prime or not.

    Args:
        number (int): Given number to check

    Returns:
        check result (bool): True if prime and False otherwise
    """
    if number == 1:
        return False
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True


def game_step() -> bool:
    """Generate question and checks user answer.

    Returns:
        bool: Correctness of the answer
    """
    # Generate random length, hidden element index and sequence
    question_value = random.randint(2, MAX_RAND_VALUE)

    # Ask user
    print('Question: {0}'.format(question_value))

    # Get correct answer
    correct_answer = 'yes' if is_prime(question_value) else 'no'

    # Get user's answer
    answer = prompt.string('Your answer: ')

    # Check user's answer
    # Print and return result of current step
    # Convert correct answer to str
    # instead of using try-catch to convert user-inputed answer to int
    if answer == correct_answer:
        print('Correct!')
        return True

    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
        answer,
        correct_answer,
    ))
    return False
