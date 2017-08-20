from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    
    # Check if values is valid
    if values is False:
        return False
    
    # Check if already solved
    if all(len(values[box]) == 1 for box in boxes): 
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    length, box = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for digit in values[box]:
        new_sudoku = values.copy()
        new_sudoku[box] = digit

        attempt = search(new_sudoku)
        if attempt:
            return attempt
