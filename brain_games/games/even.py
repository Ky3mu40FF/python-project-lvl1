"""brain-even game module."""

import random

NUM_GEN_BORDERS = (0, 20)
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    """Check if number is even.

    Args:
        num (int): The number to be checked for evenness

    Returns:
        bool: Returns True if number is even. False otherwise.
    """
    return num % 2 == 0


def generate_question_and_answer() -> str:
    """Generate question for the player and correct answer.

    Returns:
        tuple(str, str): Tuple with question and correct answer
    """
    # Get random integer value for question
    generated_number = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])

    # Generate question
    question = 'Question: {0}'.format(generated_number)

    # Get correct answer
    correct_answer = 'yes' if is_even(generated_number) else 'no'

    return (question, str(correct_answer))
