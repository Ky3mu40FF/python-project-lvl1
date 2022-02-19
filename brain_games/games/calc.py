"""brain-calc game module."""

import random

NUM_GEN_BORDERS = (0, 20)
GAME_RULES = 'What is the result of the expression?'


def calculate_expression(operator, first_operand, second_operand) -> int:
    """Calculate the given expression.

    Args:
        operator (str): Operator of the expression.
        first_operand (int): First (left) operand of the expression.
        second_operand (int): Second (right) operand of the expression.

    Returns:
        int: Result of calculation.
    """
    calculation_result = 0
    # Perform calculation
    # Python 3.8 - no pattern matching
    if operator == '+':
        calculation_result = first_operand + second_operand
    elif operator == '-':
        calculation_result = first_operand - second_operand
    elif operator == '*':
        calculation_result = first_operand * second_operand

    return calculation_result


def generate_question_and_answer() -> str:
    """Generate question for the player and correct answer.

    Returns:
        tuple(str, str): Tuple with question and correct answer
    """
    # Generating operator (+ or - or *)
    # and two random integer numbers (operands)
    operator = random.choice(('+', '-', '*'))
    first_operand = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])
    second_operand = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])

    # Generate question
    question = 'Question: {0} {1} {2}'.format(
        first_operand,
        operator,
        second_operand,
    )

    # Get correct answer
    correct_answer = calculate_expression(
        operator,
        first_operand,
        second_operand,
    )

    return (question, str(correct_answer))
