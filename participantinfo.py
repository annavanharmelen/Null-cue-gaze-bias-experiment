"""
This script contains the functions necessary for
collecting participant data.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

import random
import pandas as pd


def get_participant_details(existing_participants: pd.DataFrame):
    
    # Get participant age
    age = int(input("Participant age: "))
    
    # Generate random & unique participant number
    participant = random.randint(10,99)
    while participant in existing_participants.participant_number:
        participant = random.randint(10,99)

    # Ask for session number
    session = int(input("Session: "))
    
    return age, participant, session
