"""
This script contains the functions necessary for
seting up the computer.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023, using code by Rose Nasrawi
"""

from psychopy import visual
from psychopy.hardware.keyboard import Keyboard

def set_up(testing: bool):
    if testing:
        # laptop
        monitor = {
            'resolution': (1920, 1080), # in pixels
            'Hz': 60, # screen refresh rate in Hz
            'height': 17.5, # in cm (KLOPT DIT?)
            'distance': 50, # in cm
        }
    else:
        # lab
        monitor = {
            'resolution': (1920, 1080), # in pixels
            'Hz': 239, # screen refresh rate in Hz (KLOPT DIT?)
            'height': 38, # in cm (KLOPT DIT?)
            'distance': 60, # in cm
        }
        
    window = visual.Window(
        color = (-0.3, -0.3, -0.3),
        # monitor = 'testMonitor', 
        size = monitor['res'],
        units = 'pix',
        fullscr = True)

    mouse = visual.CustomMouse(
        win = window,
        visible = False)

    return window, Keyboard(), mouse
