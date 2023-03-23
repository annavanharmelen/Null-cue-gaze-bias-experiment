"""
This script contains the functions necessary for
creating the interactive response dial at the end of a trial.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

from psychopy import core, visual, event
from math import cos, sin, degrees, pi
import random
from trial import deg2pix

dial_step_size = (0.5*pi) / 60 # I don't understand why this is (the 60 is the refresh rate of the screen in Hz)


def turn_handle(pos, rad):

    x, y = pos
    pos = (x * cos(rad) + y * sin(rad), -x * sin(rad) + y * cos(rad))

    return pos


def get_report_orientation(key, turns):

    report_orientation = degrees(turns * dial_step_size)

    if key == "z":
        report_orientation *= -1

    return report_orientation


def evaluate_response(report_orientation, target_orientation):

    difference = abs(target_orientation - round(report_orientation))

    if difference > 90:
        difference -= 180
        difference *= -1

    performance = round(100 - difference / 90 * 100)

    return performance, difference


def getOri(tilt):

    ori = [
        random.randint(bar[tilt[0]][0], bar[tilt[0]][1]),
        random.randint(bar[tilt[1]][0], bar[tilt[1]][1]),
    ]

    return ori


def makeDial(rad, pos=(0, 0), handle=False, window):

    circle = visual.Circle(
        win=window,
        radius=rad,
        edges=deg2pix(1),
        lineWidth=deg2pix(0.05),
        lineColor='black',
        pos=pos,
    )

    if handle:
        circle.fillColor = None
    return circle


dialcirc = makeDial(deg2pix(0.15), window)
turntop = makeDial(deg2pix(0.15), pos=(0, deg2pix(1.5)), handle=True)
turnbot = makeDial(deg2pix(0.15), pos=(0, -deg2pix(1.5)), handle=True)


def response_dial(keyboard, window):

    ori = getOri("LR")

    keyboard.clearEvents()
    released = []
    pressed = []
    turns = 0

    turntop.pos = (0, dial["hpos"])
    turnbot.pos = (0, -dial["hpos"])

    dialcirc.draw()
    turntop.draw()
    turnbot.draw()

    window.flip()

    pressed = event.waitKeys(keyList=["z", "m", "q"])

    if "m" in pressed:
        key = "m"
        rad = dial_step_size
    elif "z" in pressed:
        key = "z"
        rad = -dial_step_size
    if "q" in pressed:
        core.quit()

    while released == [] and turns <= 60: #since the max amount of turns has to be less than the refresh rate, you only get 1 sec to respond

        released = keyboard.getKeys(keyList=[key], waitRelease=True, clear=True)

        turntop.pos = turn_handle(turntop.pos, rad)
        turnbot.pos = turn_handle(turnbot.pos, rad)

        turns += 1
        dialcirc.draw()
        # centerbar.draw()
        turntop.draw()
        turnbot.draw()

        window.flip()
