from utils import *

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here

    GRID_LENGTH = 81
    DIGITS = '123456789'
    
    assert len(values) == GRID_LENGTH, "Input grid must be a string of length 81 (9x9)"

    for unit in unitlist:
        for digit in DIGITS:
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
                
    return values
