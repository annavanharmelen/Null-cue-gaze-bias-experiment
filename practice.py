"""
This file contains the functions necessary for
practising the trials and the use of the report dial.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from trial import single_trial, generate_stimuli_characteristics, make_one_bar
from response import get_response


# 1. Practice response dials using a block with a specific orientation
# 2. Practice full trials

def practice(min_correct, settings):

    n_correct = 0
    while n_correct < min_correct:
        target_orientation = generate_stimuli_characteristics()['left_orientation']

        practice_bar = make_one_bar(target_orientation, [0.5, 0.5, 0.5], "middle", settings)

        report: dict = get_response(target_orientation, settings, [practice_bar])
        
        # show report on screen

        if report['performance'] > 85:
            n_correct += 1
        else:  # Force correct practice trials to be consecutive
            n_correct = 0
    
    n_correct = 0
    while n_correct < min_correct:
        stimulus = generate_stimuli_characteristics()

        report: dict = single_trial(**stimulus, settings=settings)

        # show report on screen

        if report['performance'] > 70:
            n_correct += 1
        else:  # Force correct practice trials to be consecutive
            n_correct = 0
