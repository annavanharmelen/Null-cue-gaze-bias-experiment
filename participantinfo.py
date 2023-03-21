"""
This script contains the functions necessary for
collecting participant data.
To run the 'placeholder' experiment, see main.py.

made by Anna van Harmelen, 2023
"""

import random

def get_participant_details():
    
    # Get participant age
    age = int(input("Participant age: "))
    
    # Generate random participant number
    participant = random.randint(10,99)

    # Ask for session number
    session = int(input("Session: "))
    
    return age, participant, session
