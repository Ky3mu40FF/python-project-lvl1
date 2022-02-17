"""brain-even game module."""

import random

import prompt

NUM_GEN_BORDERS = (0, 20)


def get_game_rules() -> str:
    """Brain-even game rules getter.

    Returns:
        rules text (str): Text with brain-even game rules
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def game_step() -> bool:
    """Generate question and checks user answer.

    Returns:
        bool: Correctness of the answer
    """
    # Match between even check results and correct answers
    correct_answers = {True: 'yes', False: 'no'}

    # Get random integer value for question
    generated_number = random.randint(NUM_GEN_BORDERS[0], NUM_GEN_BORDERS[1])

    # Ask user and get his answer
    print('Question: {0}'.format(generated_number))
    answer = prompt.string('Your answer: ')

    # Check if number is even and check user' answer
    is_number_even = generated_number % 2 == 0
    is_answer_correct = correct_answers[is_number_even] == answer

    # Print and return result of current step
    if is_answer_correct:
        print('Correct!')
        return True

    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
        answer, correct_answers[is_number_even],
    ))
    return False
