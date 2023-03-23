"""
Main script for running 'placeholder' experiment
made by Anna van Harmelen, 2023

see README.md for instructions if needed
"""

# Import necessary stuff
from datetime import datetime
import pandas as pd
from participantinfo import get_participant_details
from set_up import set_up
from eyetracker import Eyelinker
from argparse import ArgumentParser

def main():
    """
    Data formats / storage:
     - eyetracking data saved in one .edf file per session
     - all trial data saved in one .csv per session
     - subject data in one .csv (for all sessions combined)
    """

    # Read command-line arguments
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-t', '--test', action='store_true', help="Just do a test run, i.e. no eyetracking and we'll save the data somewhere else")
    args = parser.parse_args()
    testing = args.test

    # Initialise set-up
    window, keyboard, mouse = set_up(testing)

    # Get participant details
    pd.read_csv()

    age, participant, session = get_participant_details()
    # hier wel deze dingen saven bij de participantinfo.csv

    # Connect to eyetracker and calibrate it
    if not testing:
        eyelinker = Eyelinker(participant, session, window, directory)
        eyelinker.calibrate()

    # Start practice trials

    # Check practice performance

    # data looks like this:
    #     [{'trial_number': 1, 'reaction_time': 300, 'rotation': 45},
    #     {'trial_number': 2, 'reaction_time': 400, 'rotation': 60},
    #     {'trial_number': 3, 'reaction_time': 200, 'rotation': 38}]
    data = []

    # Start eyetracker
    if not testing:
        eyelinker.start()

    # Start experiment
    try:
        # Run trials in blocks
        for trial_number in range(10):
            trial_data = {"trial_number": trial_number}
            start_time = datetime.now()

            # some code some code
            trial_data["other_cool_stuff"] = "very cool data " * 10
            trial_data["duration"] = datetime.now() - start_time

            data.append(trial_data)

    finally:
        # sla data die je wel hebt als .csv op
        # sla ook number of trials op in proefpersonenbestand
        participant_details["ntrials"] = len(data)

    # Thanks for meedoen


if __name__ == '__main__':
    main()
