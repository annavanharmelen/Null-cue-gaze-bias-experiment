"""
This script is used to test random aspects
of the 'placeholder' experiment.

made by Anna van Harmelen, 2023
"""

from psychopy import visual
from math import atan2, degrees

import time


def deg2pix(deg):
    dpix = degrees(atan2(0.5 * 864, 1536)) / (0.5 * 1536)
    return int(deg / dpix)


window = visual.Window(color=[0, 0.6, 1], size=[1536, 864], units="pix", fullscr=True)

fixation_size = {
    "size": deg2pix(1),
    "line": deg2pix(0.2),
    #        'basecol': (0.2, 0.2, 0.2),
    #       'probecol': (0.9, 0.9, 0.9),
}

print(fixation_size["size"])
print(fixation_size["line"])

fixation_cross = visual.ShapeStim(
    win=window,
    vertices=(
        (0, -fixation_size["size"]),
        (0, fixation_size["size"]),
        (0, 0),
        (-fixation_size["size"], 0),
        (fixation_size["size"], 0),
    ),
    lineColor=[0, 0, 0],
    lineWidth=fixation_size["line"],
    closeShape=False,
    units="pix",
)

fixation_cross.draw()
window.flip()

time.sleep(2)
