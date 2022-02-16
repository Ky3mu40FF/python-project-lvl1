"""Brain-progression game module."""

import random
from typing import Tuple

import prompt

MAX_PROGRESSION_FIRST_TERM_VALUE = 100
MAX_PROGRESSION_COEFFICIENT = 10
LENGTH_BOUNDARY = (5, 10)


def get_game_rules() -> str:
    """brain-progression game rules getter.

    Returns:
        rules text (str): Text with brain-progression game rules
    """
    return 'What number is missing in the progression?'


def generate_random_sequence(num_of_terms: int) -> Tuple[int]:
    """Generate random arithmetic sequence with given length.

    Args:
        num_of_terms (int): Number of elements in arithmetic sequence

    Returns:
        sequence (Tuple[int]): Arithmetic sequence with given length
    """
    first_term = random.randint(0, MAX_PROGRESSION_FIRST_TERM_VALUE)
    coefficient = random.randint(1, MAX_PROGRESSION_COEFFICIENT)

    last_term = first_term + (num_of_terms - 1) * coefficient

    return tuple(range(first_term, last_term + 1, coefficient))


def generate_question_from_sequence(
    sequence: Tuple[int],
    element_to_hide_index: int,
) -> str:
    """Generate text version of sequence with hidden element for question.

    Args:
        sequence (sequence[int]): Arithmetic sequence
        element_to_hide_index (int): Index of the element of sequence to hide

    Returns:
        sequence_str (str): String with arithmetic sequence with hidden element
    """
    question_seq = ''

    for el in sequence:
        if sequence.index(el) == element_to_hide_index:
            question_seq = '{0}{1} '.format(question_seq, '..')
        else:
            question_seq = '{0}{1} '.format(question_seq, str(el))

    return question_seq.rstrip()


def game_step() -> bool:
    """Generate question and checks user answer.

    Returns:
        bool: Correctness of the answer
    """
    # Generate random length, hidden element index and sequence
    sequence_lenght = random.randint(LENGTH_BOUNDARY[0], LENGTH_BOUNDARY[1])
    hidden_element_index = random.randint(0, sequence_lenght - 1)
    sequence = generate_random_sequence(sequence_lenght)

    # Ask user
    print('Question: {0}'.format(
        generate_question_from_sequence(sequence, hidden_element_index),
    ))

    # Get correct answer
    correct_answer = sequence[hidden_element_index]

    # Get user's answer
    answer = prompt.string('Your answer: ')

    # Check user's answer
    # Print and return result of current step
    # Convert correct answer to str
    # instead of using try-catch to convert user-inputed answer to int
    if answer == str(correct_answer):
        print('Correct!')
        return True

    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
        answer,
        correct_answer,
    ))
    return False
