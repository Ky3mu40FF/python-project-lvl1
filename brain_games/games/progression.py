"""Brain-progression game module."""

import random
from typing import Tuple

GAME_RULES = 'What number is missing in the progression?'
INITIAL_TERM_BOUNDARIES = (0, 100)
COMMON_DIFFERENCE_BOUNDARIES = (5, 10)
NUM_OF_TERMS_BOUNDARIES = (5, 10)


def generate_arithmetic_sequence(
    initial_term: int,
    common_difference: int,
    num_of_terms: int,
) -> Tuple[int]:
    """Generate arithmetic sequence.

    Args:
        initial_term (int): Initial term of an arithmetic sequence.
        common_difference (int): Constant difference between consecutive terms.
        num_of_terms (int): Number of terms in arithmetic sequence.

    Returns:
        Tuple[int]: Arithmetic sequence with given length
    """
    last_term = initial_term + (num_of_terms - 1) * common_difference
    return tuple(range(initial_term, last_term + 1, common_difference))


def generate_question_from_sequence(
    sequence: Tuple[int],
    element_to_hide_index: int,
) -> str:
    """Generate text version of sequence with hidden element for question.

    Args:
        sequence (sequence[int]): Arithmetic sequence
        element_to_hide_index (int): Index of the element of sequence to hide

    Returns:
        str: String with arithmetic sequence with hidden element
    """
    return ' '.join([
        '..' if index == element_to_hide_index
        else str(element)
        for index, element in enumerate(sequence)
    ])


def generate_question_and_answer() -> Tuple[str, str]:
    """Generate question for the player and correct answer.

    Returns:
        Tuple[str, str]: Tuple with question and correct answer
    """
    sequence = generate_arithmetic_sequence(
        initial_term=random.randint(*INITIAL_TERM_BOUNDARIES),
        common_difference=random.randint(*COMMON_DIFFERENCE_BOUNDARIES),
        num_of_terms=random.randint(*NUM_OF_TERMS_BOUNDARIES),
    )
    element_to_hide_index = random.randint(0, len(sequence) - 1)

    question = generate_question_from_sequence(
        sequence,
        element_to_hide_index,
    )
    correct_answer = sequence[element_to_hide_index]
    return question, str(correct_answer)
