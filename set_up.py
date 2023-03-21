"""
This script contains the functions necessary for
seting up the computer.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023, using code by Rose Nasrawi
"""

from psychopy import visual
from psychopy.hardware import keyboard

def set_up():
    window = visual.Window(
        color = monitor['col'],
        # monitor = 'testMonitor', 
        size = monitor['res'],
        units = 'pix',
        fullscr = True)

    kboard = keyboard.Keyboard()

    mouse = visual.CustomMouse(
        win = window,
        visible = False)

    return window, kboard, mouse
