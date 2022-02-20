"""brain-calc game module."""

import random
from operator import add, mul, sub
from types import MappingProxyType  # Immutable dict for constant (WPS407)
from typing import Tuple

GAME_RULES = 'What is the result of the expression?'
NUM_GEN_BORDERS = (0, 20)
SIGN_TO_FUNCTION = MappingProxyType({'+': add, '-': sub, '*': mul})


def calculate_expression(
    operator: str,
    first_operand: int,
    second_operand: int,
) -> int:
    """Calculate the given expression.

    Args:
        operator (str): Operator of the expression. Ex. '-', '+', '*' etc.
        first_operand (int): First (left) operand of the expression.
        second_operand (int): Second (right) operand of the expression.

    Returns:
        int: Result of calculation.
    """
    operation = SIGN_TO_FUNCTION.get(operator)
    return operation(first_operand, second_operand)


def generate_question_and_answer() -> Tuple[str, str]:
    """Generate question for the player and correct answer.

    Returns:
        Tuple[str, str]: Tuple with question and correct answer
    """
    operator = random.choice(('+', '-', '*'))
    first_operand = random.randint(*NUM_GEN_BORDERS)
    second_operand = random.randint(*NUM_GEN_BORDERS)

    question = '{0} {1} {2}'.format(
        first_operand,
        operator,
        second_operand,
    )
    correct_answer = calculate_expression(
        operator,
        first_operand,
        second_operand,
    )
    return question, str(correct_answer)
