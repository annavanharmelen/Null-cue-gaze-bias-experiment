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
from trial import single_trial, generate_stimuli_characteristics
from time import time
from practice import practice
import datetime as dt

def main():
    """
    Data formats / storage:
     - eyetracking data saved in one .edf file per session
     - all trial data saved in one .csv per session
     - subject data in one .csv (for all sessions combined)
    """

    # Read command-line arguments
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Just do a test run, i.e. no eyetracking and we'll save the data somewhere else",
    )
    args = parser.parse_args()
    # testing = args.test
    testing = True

    # Initialise set-up
    settings = set_up(testing)
    start_of_experiment = time()

    # Get participant details and save in same file as before
    old_participants = pd.read_csv(rf"{settings['directory']}\participantinfo.csv")
    new_participants = get_participant_details(old_participants, testing)

    # Connect to eyetracker and calibrate it
    if not testing:
        eyelinker = Eyelinker(
            new_participants.participant_number.iloc[-1],
            new_participants.session_number.iloc[-1],
            settings['window'],
            settings['directory'],
        )
        eyelinker.calibrate()

    # Practice (also checks performance)
    practice(3, settings)

    # Initialise some stuff
    data = []
    current_trial = 0

    # Start eyetracker
    if not testing:
        eyelinker.start()

    # Start experiment
    try:
        amount_of_trials = 5

        for trial in range(amount_of_trials):

            current_trial += 1
            start_time = time()

            stimuli_characteristics: dict = generate_stimuli_characteristics()

            # Generate trial
            report: dict = single_trial(**stimuli_characteristics, settings=settings)
            end_time = time()

            # Save trial data
            data.append(
                {
                    "trial_number": current_trial,
                    #'reaction_time': reaction_time,
                    "start_time": str(dt.timedelta(seconds = (start_time - start_of_experiment))),
                    "end_time": str(dt.timedelta(seconds = (end_time - start_of_experiment))),
                    **stimuli_characteristics,
                    **report
                }
            )  # vergeet niet ook tzt op te slaan welke bar de target was

    finally:
        
        # Stop eyetracker (this should also save the data)
        if not testing:
            eyelinker.stop()

        # Save all collected trial data to a new .csv
        pd.DataFrame(data).to_csv(
            rf"{settings['directory']}\data_session_{new_participants.session_number.iloc[-1]}.csv",
            index=False,
        )

        # Register how many trials this participant has completed
        new_participants.loc[new_participants.index[-1], "trials_completed"] = len(data)

        # Save participant data to existing .csv file
        new_participants.to_csv(
            rf"{settings['directory']}\participantinfo.csv", index=False
        )


    # Thanks for meedoen


if __name__ == "__main__":
    main()
