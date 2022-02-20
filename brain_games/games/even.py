"""brain-even game module."""

import random
from types import MappingProxyType  # Immutable dict for constant (WPS407)
from typing import Tuple

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_GEN_BORDERS = (0, 20)
IS_EVEN_TO_CORRECT_ANSWER = MappingProxyType({True: 'yes', False: 'no'})


def is_even(num: int) -> bool:
    """Check if number is even.

    Args:
        num (int): The number to be checked for evenness

    Returns:
        bool: Returns True if number is even. False otherwise.
    """
    return num % 2 == 0


def generate_question_and_answer() -> Tuple[str, str]:
    """Generate question for the player and correct answer.

    Returns:
        Tuple[str, str]: Tuple with question and correct answer
    """
    generated_number = random.randint(*NUM_GEN_BORDERS)
    question = str(generated_number)
    correct_answer = IS_EVEN_TO_CORRECT_ANSWER.get(is_even(generated_number))
    return question, str(correct_answer)
