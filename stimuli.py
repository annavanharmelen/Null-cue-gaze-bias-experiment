"""
This script contains the functions necessary for
creating the fixation cross and the bar stimuli.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from psychopy import visual
from math import atan2, degrees


def deg2pix(deg):
    dpix = degrees(atan2(0.5 * monitor['h'], monitor['d'])) / (0.5 * monitor['res'][0])
    return int(deg / dpix)


def create_fixation_cross(window):

    # Determine size of fixation cross
    fixation_size = {
        'size': deg2pix(0.2),
        'line': deg2pix(0.05),
        'basecol': (0.2, 0.2, 0.2),
        'probecol': (0.9, 0.9, 0.9),
    }

    # Create fixation cross
    fixation_cross = visual.ShapeStim(
        win=window,
        vertices=(
            (0, -fixation_size['size']),
            (0, fixation_size['size']),
            (0, 0),
            (-fixation_size['size'], 0),
            (fixation_size['size'], 0),
        ),
        lineWidth=fixation_size['line'],
        closeShape=False,
        units='pix',
    )

    return fixation_cross


def make_one_bar(position, window):

    bar_stimulus = visual.Rect(
        win=window, units='pix', width=bar['size'][0], height=bar['size'][1], pos=position
    )

    return bar_stimulus

def create_stimuli_frame():
    return 0
