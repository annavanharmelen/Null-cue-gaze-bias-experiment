"""
This file contains the functions necessary for
creating the interactive response dial at the end of a trial.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from psychopy import core, visual, event
from psychopy.hardware.keyboard import Keyboard
from math import cos, sin, degrees


def turn_handle(pos, dial_step_size):

    x, y = pos
    pos = (
        x * cos(dial_step_size) + y * sin(dial_step_size),
        -x * sin(dial_step_size) + y * cos(dial_step_size),
    )

    # centre, distance, rad
    return pos


def get_report_orientation(key, turns, dial_step_size):

    report_orientation = degrees(turns * dial_step_size)

    if key == "z":
        report_orientation *= -1

    return report_orientation


def evaluate_response(report_orientation, target_orientation):
    report_orientation = round(report_orientation)

    difference = abs(target_orientation - report_orientation)

    if difference > 90:
        difference -= 180
        difference *= -1

    performance = round(100 - difference / 90 * 100)

    return {
        "report_orientation": report_orientation,
        "performance": performance,
        "difference": difference,
    }


def make_circle(rad, settings, pos=(0, 0), handle=False):

    circle = visual.Circle(
        win=settings["window"],
        radius=settings["deg2pix"](rad),
        edges=settings["deg2pix"](1),
        lineWidth=settings["deg2pix"](0.05),
        fillColor=None,
        pos=(settings["deg2pix"](pos[0]), settings["deg2pix"](pos[1])),
    )

    if handle:
        circle.lineColor = "black"
    else:
        circle.lineColor = [-0.5, -0.5, -0.5]

    return circle


def make_dial(settings):
    dial_circle = make_circle(1.5, settings)
    top_dial = make_circle(
        0.15,
        settings,
        pos=(0, 1.5),
        handle=True,
    )
    bottom_dial = make_circle(
        0.15,
        settings,
        pos=(0, -1.5),
        handle=True,
    )

    return dial_circle, top_dial, bottom_dial


def get_response(target_orientation, settings, additional_objects=[]):

    keyboard: Keyboard = settings["keyboard"]
    window = settings["window"]

    keyboard.clearEvents()
    turns = 0

    dial_circle, top_dial, bottom_dial = make_dial(settings)

    for item in additional_objects:
        item.draw()

    dial_circle.draw()
    top_dial.draw()
    bottom_dial.draw()


    window.flip()

    # Wait indefinitely until the participant starts giving an answer
    pressed = event.waitKeys(keyList=["z", "m", "q"])

    if "m" in pressed:
        key = "m"
        rad = settings["dial_step_size"]
    elif "z" in pressed:
        key = "z"
        rad = -settings["dial_step_size"]
    if "q" in pressed:
        core.quit()

    # Stop rotating the moment either of the following happens:
    # - the participant released the rotation key
    # - a second passed

    while not keyboard.getKeys(keyList=[key]) and turns <= settings["monitor"]["Hz"]:

        top_dial.pos = turn_handle(top_dial.pos, rad)
        bottom_dial.pos = turn_handle(bottom_dial.pos, rad)

        turns += 1

        for item in additional_objects:
            item.draw()
        
        dial_circle.draw()
        top_dial.draw()
        bottom_dial.draw()

        window.flip()

    return evaluate_response(
        get_report_orientation(key, turns, settings["dial_step_size"]),
        target_orientation,
    )
