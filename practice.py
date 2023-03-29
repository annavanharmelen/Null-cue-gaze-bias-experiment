"""
This file contains the functions necessary for
practising the trials and the use of the report dial.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from trial import (
    single_trial,
    generate_stimuli_characteristics,
    make_one_bar,
    show_text,
)
from response import get_response, wait_for_key
from psychopy import event
from psychopy.hardware.keyboard import Keyboard
from time import sleep

# 1. Practice response dials using a block with a specific orientation
# 2. Practice full trials


def practice(min_correct, settings):

    # Show explanation
    show_text(
        f"Welcome to the practice trials. You must complete {min_correct} trials consecutively in a row to finish the practice session. \
            \nPress the space bar to start the practice session.",
        settings["window"],
    )
    settings["window"].flip()
    wait_for_key(["space"], settings["keyboard"])

    # Practice dial until perfect
    n_correct = 0
    while n_correct < min_correct:
        practice_dial_colour = [0.5, 0.5, 0.5]

        target = generate_stimuli_characteristics()
        target_orientation = target['target_orientation']
        target_colour = practice_dial_colour

        practice_bar = make_one_bar(
            target_orientation, practice_dial_colour, "middle", settings
        )

        report: dict = get_response(target_orientation, target_colour, settings, [practice_bar])

        if report["performance"] > 90:
            n_correct += 1
        else:  # Force correct practice trials to be consecutive
            n_correct = 0

        show_text(f"{report['performance']}", settings["window"])
        settings["window"].flip()
        sleep(0.8)

    # Practice trials until perfect
    n_correct = 0
    while n_correct < min_correct:
        stimulus = generate_stimuli_characteristics()

        report: dict = single_trial(**stimulus, settings=settings)

        if report["performance"] > 75:
            n_correct += 1
        else:  # Force correct practice trials to be consecutive
            n_correct = 0

        show_text(f"{report['performance']}", settings["window"])
        settings["window"].flip()
        sleep(0.8)

    # Finished! 
    show_text(
        f"You successfully finished the practice trials!\nPress the space bar to start the experiment.",
        settings["window"],
    )
    settings["window"].flip()
    wait_for_key(["space"], settings["keyboard"])
