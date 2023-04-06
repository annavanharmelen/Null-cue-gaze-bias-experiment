"""
This file contains the functions necessary for
seting up the computer.
To run the 'null-cue gaze bias' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from psychopy import visual
from psychopy.hardware.keyboard import Keyboard
from math import degrees, atan2, pi


def set_up(testing: bool):
    if testing:
        # laptop
        monitor = {
            "resolution": (1920, 1080),  # in pixels
            "Hz": 60,  # screen refresh rate in Hz
            "width": 33,  # in cm (KLOPT DIT?)
            "distance": 50,  # in cm
        }

        directory = r"C:\Users\annav\Documents\Jottacloud\Neuroscience\Year 2\Master's thesis\Code\Anna's code - 20.03.2023\data"

    else:
        # lab
        monitor = {
            "resolution": (1920, 1080),  # in pixels
            "Hz": 239,  # screen refresh rate in Hz (KLOPT DIT?)
            "width": 38,  # in cm (KLOPT DIT?)
            "distance": 60,  # in cm
        }

        directory = r"bloepediebloepbloep"

    window = visual.Window(
        color=('#7F7F7F'),
        monitor = monitor,
        size=monitor["resolution"],
        units="pix",
        fullscr=True,
    )

    degrees_per_pixel = degrees(atan2(0.5 * monitor["width"], monitor["distance"])) / (
        0.5 * monitor["resolution"][0]
    )

    return dict(
        deg2pix=lambda deg: round(deg / degrees_per_pixel),
  
        # move the dial a quarter circle per second
        dial_step_size=(0.5 * pi) / monitor["Hz"],  

        window=window,

        keyboard=Keyboard(),

        mouse=visual.CustomMouse(win=window, visible=False),

        monitor=monitor,

        directory=directory,
    )
