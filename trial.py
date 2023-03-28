"""
This file contains the functions necessary for
creating the fixation cross and the bar stimuli,
and then run a single trial start-to-finish.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from psychopy import visual
from math import atan2, degrees
from psychopy.core import wait
from time import time
from response import get_response
import random

# experiment flow:
# 1. fixatiekruis
# 2. fixatiekruis + twee blokkies ernaast
# 3. fixatiekruis
# 4. fixatiekruis + vierkantje om het kruis
# 5. fixatiekruis
# 6. probecue
# 7. dials voor respons van proefpersoon

ECCENTRICITY = 6


def generate_stimuli_characteristics():

    return {
        "stimuli_colours": random.sample(["blue", "red", "green", "yellow"], 2),
        "capture_colour": random.choice(["red", "blue", "green"]),
        "left_orientation": random.randint(-80, 80),
        "right_orientation": random.randint(-80, 80),
        "target_bar": random.choice(["left", "right"]),
    }


def create_fixation_cross(settings):
    _cached_fixation_cross = None

    # Create fixation cross
    if _cached_fixation_cross is None:
        # Determine size of fixation cross
        fixation_size = settings["deg2pix"](0.2)

        _cached_fixation_cross = visual.ShapeStim(
            win=settings["window"],
            vertices=(
                (0, -fixation_size),
                (0, fixation_size),
                (0, 0),
                (-fixation_size, 0),
                (fixation_size, 0),
            ),
            lineWidth=settings["deg2pix"](0.05),
            lineColor=[0, 0, 0],
            closeShape=False,
            units="pix",
        )

    _cached_fixation_cross.draw()


def make_one_bar(orientation, colour, position, settings):

    # Check input
    if position == "left":
        pos = (-settings["deg2pix"](ECCENTRICITY), 0)
    elif position == "right":
        pos = (settings["deg2pix"](ECCENTRICITY), 0)
    elif position == "middle":
        pos = (0, 0)
    else:
        raise Exception(f"Expected 'left' or 'right', but received {position!r}. :(")

    # Create bar stimulus
    bar_stimulus = visual.Rect(
        win=settings["window"],
        units="pix",
        width=settings["deg2pix"](0.4),
        height=settings["deg2pix"](3),
        pos=pos,
        ori=orientation,
        fillColor=colour,
    )

    return bar_stimulus


def create_stimuli_frame(left_orientation, right_orientation, colours, settings):

    create_fixation_cross(settings)
    make_one_bar(left_orientation, colours[0], "left", settings).draw()
    make_one_bar(right_orientation, colours[1], "right", settings).draw()


def create_capture_cue_frame(colour, settings):

    capture_cue = visual.Rect(
        win=settings["window"],
        units="pix",
        width=settings["deg2pix"](2),
        height=settings["deg2pix"](2),
        pos=(0, 0),
        lineColor=colour,
        lineWidth=settings["deg2pix"](0.1),
        fillColor=None,
    )

    capture_cue.draw()
    create_fixation_cross(settings)


def create_response_dials(iets):
    ...


def do_while_showing(waiting_time, something_to_do, window):
    """
    Show whatever is drawn to the screen for exactly `waiting_time` period,
    while doing `something_to_do` in the mean time.
    """
    window.flip()
    start = time()
    something_to_do()
    wait(waiting_time - (time() - start))


def single_trial(
    left_orientation,
    right_orientation,
    target_bar,
    stimuli_colours,
    capture_colour,
    settings,
):

    screens = [
        (0, lambda: 0 / 0),  # initial one to make life easier
        (0.1, lambda: create_fixation_cross(settings)),
        (
            0.25,
            lambda: create_stimuli_frame(
                left_orientation, right_orientation, stimuli_colours, settings
            ),
        ),
        (0.75, lambda: create_fixation_cross(settings)),
        (0.25, lambda: create_capture_cue_frame(capture_colour, settings)),
        (1.75, lambda: create_fixation_cross(settings)),
        # (None, lambda: create_response_dials(window))
    ]

    # !!! The timing you pass to do_while_showing is the timing for the previously drawn screen.

    for index, (duration, _) in enumerate(screens[:-1]):
        # Draw the next screen while showing the current one
        do_while_showing(duration, screens[index + 1][1], settings["window"])

    return get_response(
        left_orientation if target_bar == "left" else right_orientation, settings
    )
