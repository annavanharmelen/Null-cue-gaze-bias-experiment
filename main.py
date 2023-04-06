"""
Main script for running the 'null-cue gaze bias' experiment
made by Anna van Harmelen, 2023

see README.md for instructions if needed
"""

# Import necessary stuff
from datetime import datetime
from psychopy import core
import pandas as pd
from participantinfo import get_participant_details
from set_up import set_up
from eyetracker import Eyelinker
from argparse import ArgumentParser
from trial import single_trial, generate_stimuli_characteristics
from time import time
from practice import practice
import datetime as dt
from block import create_block, block_break, long_break, finish, quick_finish

N_BLOCKS = 4
TRIALS_PER_BLOCK = 6


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
    practice(settings)
    
    # Start eyetracker
    if not testing:
        eyelinker.start()

    # Initialise some stuff
    data = []
    current_trial = 0
    blocks_done = 0

    # Start experiment
    try:
        for block in range(N_BLOCKS):

            # Pseudo-randomly create conditions and target locations (so they're weighted)
            block_info = create_block(TRIALS_PER_BLOCK)

            # Run trials per pseudo-randomly created info
            for condition, target_bar in block_info:

                current_trial += 1
                start_time = time()

                stimuli_characteristics: dict = generate_stimuli_characteristics(condition, target_bar)

                # Generate trial
                report: dict = single_trial(**stimuli_characteristics, settings=settings)
                end_time = time()
              
                # Save trial data
                data.append(
                    {
                        "trial_number": current_trial,
                        "block": block+1,
                        "start_time": str(dt.timedelta(seconds = (start_time - start_of_experiment))),
                        "end_time": str(dt.timedelta(seconds = (end_time - start_of_experiment))),
                        **stimuli_characteristics,
                        **report
                    }
                )
            
            # Break after end of block, unless it's the last block.
            blocks_done += 1

            if block + 1 == N_BLOCKS // 2:
                long_break(N_BLOCKS, settings)
            elif block + 1 < N_BLOCKS:
                block_break(block + 1, N_BLOCKS, settings)


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

        # Done!
        if blocks_done == N_BLOCKS: 
            finish(N_BLOCKS, settings)
        else:
            quick_finish(settings)
        core.quit()


    # Thanks for meedoen


if __name__ == "__main__":
    main()
