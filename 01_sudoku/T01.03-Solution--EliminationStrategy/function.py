from utils import *

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    
    GRID_LENGTH = 81
    
    assert len(values) == GRID_LENGTH, "Input grid must be a string of length 81 (9x9)"
    
    for key, value in values.items():
        if len(value) == 1:
            for peer in peers[key]:
                values[peer] = values[peer].replace(value, '')

    return values
