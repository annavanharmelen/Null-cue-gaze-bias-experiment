"""
This script contains the functions necessary for
creating the fixation cross and the bar stimuli.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from psychopy import visual
from math import atan2, degrees
from psychopy.core import wait
from time import time

# Create stimuli frames
# What changes per trial: orientation of two blocks (int between 0 and 360), colours of both blocks (from set selection) (list of four rgb values)

# experiment flow:
# 1. fixatiekruis
# 2. fixatiekruis + twee blokkies ernaast
# 3. fixatiekruis
# 4. fixatiekruis + vierkantje om het kruis
# 5. fixatiekruis
# 6. dials voor respons van proefpersoon

ECCENTRICITY = 6


def deg2pix(deg, monitor):
    dpix = degrees(atan2(0.5 * monitor["h"], monitor["d"])) / (0.5 * monitor["res"][0])
    return round(deg / dpix)

px_per_degree
# we waren bezig met:
# is dit degrees per pixel of pixels per degree?
# en: moet monitor:h de hoogte of de breedte van het scherm zijn en waarom heet het dan 'h'?
# en dat magic number van dpix kan dan beter naar set-up


_cached_fixation_cross = None


def create_fixation_cross(window, monitor):
    """
    This function determines the size of the fixation cross and creates the shape, but does not draw it or flip the window.
    """
    # Create fixation cross
    if _cached_fixation_cross is None:

        # Determine size of fixation cross
        fixation_size = deg2pix(0.2, monitor)

        _cached_fixation_cross = visual.ShapeStim(
            win=window,
            vertices=(
                (0, -fixation_size),
                (0, fixation_size),
                (0, 0),
                (-fixation_size, 0),
                (fixation_size, 0),
            ),
            lineWidth=deg2pix(0.05),
            lineColor=[0, 0, 0],
            closeShape=False,
            units="pix",
        )

    _cached_fixation_cross.draw()


def make_one_bar(orientation, colour, position, window):

    # Check input
    if position == "left":
        pos = [-deg2pix(ECCENTRICITY), 0]
    elif position == "right":
        pos = [deg2pix(ECCENTRICITY), 0]
    else:
        raise Exception(f"Expected 'left' or 'right', but received {position!r}. :(")

    # Create bar stimulus
    bar_stimulus = visual.Rect(
        win=window,
        units="pix",
        width=deg2pix(0.4),
        height=deg2pix(3),
        pos=pos,
        ori=orientation,
        fillColor=colour,
    )

    bar_stimulus.draw()


def create_stimuli_frame(orientations, colours, window):

    create_fixation_cross(window)
    make_one_bar(orientations[0], colours[0], "left", window)
    make_one_bar(orientations[1], colours[1], "right", window)

def create_capture_cue(iets):
    ...

def create_response_dials(iets):
    ...

def get_response(iets):
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


def single_trial(orientations, stimuli_colours, capture_colour, window):
    screens = [
     (0, lambda: 0 / 0),  # initial one to make life easier
     (0.1, lambda: create_fixation_cross(window)),
     (0.25, lambda: create_stimuli_frame(orientations, stimuli_colours, window)),
     (0.75, lambda: create_fixation_cross(window)),
     (0.25, lambda: create_capture_cue(capture_colour, window)),
     (1.75, lambda: create_fixation_cross(window)),
     (None, lambda: create_response_dials(window))  # draw _something_ to make sure the timing is correct
    ]

    # !!! The timing you pass to do_while_showing is the timing for the previously drawn screen.

    for index, (duration, _) in enumerate(screens[:-1]):
        # Draw the next screen while showing the current one
        do_while_showing(duration, screens[index+1][1])
    
    return get_response(window)
