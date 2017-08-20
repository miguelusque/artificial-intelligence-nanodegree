from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    GRID_LENGTH = 81
    EMPTY_VALUE = '.'
    ANY_VALUE = '123456789'
    
    assert len(grid) == GRID_LENGTH, "Input grid must be a string of length 81 (9x9)"
    
    result = {}
    for i in range(GRID_LENGTH):
         result[boxes[i]] = grid[i] if grid[i] != EMPTY_VALUE else ANY_VALUE
    
    return result