"""Brain-prime game module."""

import math
import random
from types import MappingProxyType  # Immutable dict for constant (WPS407)
from typing import Tuple

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUM_GEN_BORDERS = (1, 10)
IS_PRIME_TO_CORRECT_ANSWER = MappingProxyType({True: 'yes', False: 'no'})


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


def generate_question_and_answer() -> Tuple[str, str]:
    """Generate question for the player and correct answer.

    Returns:
        Tuple[str, str]: Tuple with question and correct answer
    """
    generated_number = random.randint(*NUM_GEN_BORDERS)
    question = str(generated_number)
    correct_answer = IS_PRIME_TO_CORRECT_ANSWER.get(is_prime(generated_number))
    return question, str(correct_answer)
