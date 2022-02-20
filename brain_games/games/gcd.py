"""brain-gcd game module."""

import random
from typing import Tuple

GAME_RULES = 'Find the greatest common divisor of given numbers.'
NUM_GEN_BORDERS = (1, 200)


def calculate_gcd(num1: int, num2: int) -> int:
    """Calculate the greatest common division (GCD) of two numbers.

    Args:
        num1 (int): First number.
        num2 (int): Second number.

    Returns:
        int: Greatest common division (GCD) of two numbers.
    """
    # Make a life a little easier
    # Greater number is first
    if num1 < num2:
        num1, num2 = num2, num1

    gcd = 0

    # The Euclidean algorithm
    while True:
        remainder = num1 % num2
        if remainder == 0:
            gcd = num2
            break
        else:
            num1, num2 = num2, remainder

    return gcd


def generate_question_and_answer() -> Tuple[str, str]:
    """Generate question for the player and correct answer.

    Returns:
        Tuple[str, str]: Tuple with question and correct answer
    """
    num1, num2 = random.sample(
        range(*NUM_GEN_BORDERS),
        2,
    )
    question = '{0} {1}'.format(
        num1,
        num2,
    )
    correct_answer = calculate_gcd(num1, num2)
    return question, str(correct_answer)
