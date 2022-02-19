"""Brain-prime game module."""

import math
import random

MAX_RAND_VALUE = 10
GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Check if given number is prime or not.

    Args:
        number (int): Given number to check if it is prime or not

    Returns:
        bool: True if given number is prime. False otherwise
    """
    if number == 1:
        return False

    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False

    return True


def generate_question_and_answer() -> str:
    """Generate question for the player and correct answer.

    Returns:
        tuple(str, str): Tuple with question and correct answer
    """
    # Generate random integer positive number
    question_value = random.randint(2, MAX_RAND_VALUE)

    # Generate question
    question = 'Question: {0}'.format(question_value)

    # Get correct answer
    correct_answer = 'yes' if is_prime(question_value) else 'no'

    return (question, str(correct_answer))
