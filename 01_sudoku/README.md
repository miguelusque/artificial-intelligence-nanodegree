# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: This technique consists of finding boxes in the same line (horizontal or vertical) with the same candidate values (e.g. A1: '23' and A3: '23').
   Once these boxes are found, we have a constraint that lets us state that any possible digit in these boxes can only be placed in the previously identified boxes (i.e. {A1, A3}). This also means that none of the others boxes in the same line can ever contain any of those candidate values; therefore the candidate values can be safely removed from the other boxes in the same line as the previously identified *naked twins*. It can be said that we have found some boxes in a specific state which lets us reduce the complexity of the problem to be resolved and therefore be closer to a solution.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Within the diagonal sudoku problem we find the following contraint: *neither horizontal nor vertical diagonals can contain any duplicated value*.
   This constraint allows the algorithim to discard any candidate value which is already solved in any of the diagonals to which the box belongs.
   In our implementation, horizontal and vertical diagonals are added to the peers set in order to ensure that the peers validation includes them.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
