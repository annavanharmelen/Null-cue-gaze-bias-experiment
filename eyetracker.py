"""
This file contains the functions necessary for
connecting and using the eyetracker.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023, using code by Rose Nasrawi
"""

from lib import eyelinker
from psychopy import event
import os


class Eyelinker:
    """
    usage:

       from eyetracker import Eyelinker

    To initialise:

       eyelinker = Eyelinker(participant, session, window, directory)
       eyelinker.calibrate()
    """

    def __init__(self, participant, session, window, directory) -> None:
        """
        This also connects to the tracker
        """

        self.directory = directory
        self.window = window
        self.tracker = eyelinker.EyeLinker(
            window=window, eye="BOTH", filename=f"rn6-{participant}-{session}.edf"
        )

    def start(self):
        os.chdir(self.directory)

        self.tracker.open_edf()
        self.tracker.init_tracker()
        self.tracker.start_recording()

    def calibrate(self):
        self.tracker.stop_recording()

        # calibwait.draw() - draws text on screen while calibrating the eye-tracker
        self.window.flip()
        event.waitKeys(keyList="r")
        self.tracker.start_recording()

    def stop(self):
        os.chdir(self.directory)

        self.tracker.stop_recording()
        self.tracker.transfer_edf()
        self.tracker.close_edf()
