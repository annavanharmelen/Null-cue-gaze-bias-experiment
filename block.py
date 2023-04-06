"""
This file contains the functions necessary for
creating and running a full block of trials start-to-finish.
To run the 'null-cue gaze bias' experiment, see main.py.

made by Anna van Harmelen, 2023
"""
import random

def create_block(n_trials):
    if n_trials % 6 != 0:
        raise Exception("Expected number of trials to be divisible by 6.")

    trials = (n_trials // 6) * list(zip(2 * ['neutral', 'congruent', 'incongruent'], 3 * ['left', 'right']))
    random.shuffle(trials)

    return trials
