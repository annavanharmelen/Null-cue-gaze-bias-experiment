"""
This script contains the functions necessary for
connecting and using the eyetracker.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023, using code by Rose Nasrawi
"""

from eyelinkPackages import eyelinker

import os

from stimuli import window, calibwait


def connectTracker(subject, session):
    tracker = eyelinker.EyeLinker(
        window=window, eye="BOTH", filename="rn6_" + subject + session + ".edf"
    )

    return tracker


def startTracker(tracker):
    os.chdir(eyedir)

    tracker.open_edf()
    tracker.init_tracker()
    tracker.start_recording()


def calibrateTracker(tracker):
    tracker.stop_recording()

    calibwait.draw()
    window.flip()
    event.waitKeys(keyList="r")

    tracker.start_recording()


def stopTracker(tracker):
    os.chdir(eyedir)

    tracker.stop_recording()
    tracker.transfer_edf()
    tracker.close_edf()
