"""
Main script for running 'placeholder' experiment
made by Anna van Harmelen, 2023

see README.md for instructions if needed
"""

# Import necessary stuff
from datetime import datetime


def main():
    """
    Data formats / storage:
     - eyetracking data saved in one .edf file per session
     - all trial data saved in one .csv per session
     - subject data in one .csv (for all sessions combined)
    """

    # Initialise set-up
    #   Check screen, keyboard, mouse etc. met een functie!!

    # Connect to eyetracker

    # Get participant details
    age = input("")
    participant_details = get_participant_details()

    # Start practice trials

    # Check practice performance
    # class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

    # columnsIndex or array-like

    # Column labels to use for resulting frame when data does not have them, defaulting to RangeIndex(0, 1, 2, …, n). If data contains column labels, will perform column selection instead.

    # Do experiment
    # data = [
    #     {'trial_number': 1, 'reaction_time': 300, 'rotation': 45},
    #     {'trial_number': 2, 'reaction_time': 400, 'rotation': 60},
    #     {'trial_number': 3, 'reaction_time': 200, 'rotation': 38}]
    data = []

    try:
        # here we run trials in blocks
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


if __name__ == "__main__":
    main()
