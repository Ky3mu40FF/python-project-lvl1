"""brain-calc game module."""

import random

import prompt

NUM_GEN_BORDERS = (0, 20)


def get_game_rules() -> str:
    """Brain-calc game rules getter.

    Returns:
        rules text (str): Text with brain-calc game rules
    """
    return 'What is the result of the expression?'


def game_step() -> bool:
    """Generate question and checks user answer.

    Returns:
        bool: Correctness of the answer
    """
    operator = random.choice(('+', '-', '*'))
    first_operand = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])
    second_operand = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])

    correct_answer = 0
    # Perform calculation
    # Python 3.8 - no pattern matching
    if operator == '+':
        correct_answer = first_operand + second_operand
    elif operator == '-':
        correct_answer = first_operand - second_operand
    elif operator == '*':
        correct_answer = first_operand * second_operand

    # Ask user and get his answer
    print('Question: {0} {1} {2}'.format(
        first_operand,
        operator,
        second_operand,
    ))
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
