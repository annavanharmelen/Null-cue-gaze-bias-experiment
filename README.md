# PLACEHOLDER

# ***[work in progress]***

Temporal visuo-motor working memory task (REVIEW), programmed in Python.


## Author
Made by Anna van Harmelen in 2023, based on code by Rose Nasrawi, see: [TemporalAction-main](https://github.com/rosenasrawi/TemporalAction).

## Installation
This experiment was created using the [PsychoPy library](https://www.psychopy.org), e.g. follow [these instructions](https://www.psychopy.org/download.html).

Additionally, you must also install the [EyeLink developer kit](https://www.sr-research.com/support/thread-13.html).

Then, you must install the PyLink library, using [these instructions](https://www.sr-research.com/support/thread-48.html).
To install using pip:

```
conda activate psychopy
pip install --index-url=https://pypi.sr-support.com sr-research-pylink
```

## Configuration
To make sure the experiment runs correctly, open the set_up.py file to enter the correct specifications of your monitor and set-up on lines 17-35.

## Running
The experiment runs in its entirety (including practice trials and explanation) if you run `python main.py`.
