# Solving a Sudoku with AI
This repository contains the 'sudoku' project of the Udacity's [Artificial Intelligence Nanodegree](https://www.udacity.com/course/artificial-intelligence-nanodegree--nd889).

![Sudoku cover](https://raw.githubusercontent.com/miguelangel/artificial-intelligence--sudoku/master/cover.jpg)

In this project, an AI agent will be implemented to solve the Sudoku game.

The agent will make use of the following techniques:

## Technique 1: Naked Twins
Q: How do we use constraint propagation to solve the naked twins problem?

A: This technique consists of finding boxes in the same line (horizontal or vertical) with the same candidate values (e.g. A1: '23' and A3: '23').
   Once these boxes are found, we have a constraint that lets us state that any possible digit in these boxes can only be placed in the previously identified boxes (i.e. {A1, A3}). This also means that none of the others boxes in the same line can ever contain any of those candidate values; therefore the candidate values can be safely removed from the other boxes in the same line as the previously identified *naked twins*. It can be said that we have found some boxes in a specific state which lets us reduce the complexity of the problem to be resolved and therefore be closer to a solution.

## Technique 2: Diagonal Sudoku
Q: How do we use constraint propagation to solve the diagonal sudoku problem?

A: Within the diagonal sudoku problem we find the following contraint: *neither horizontal nor vertical diagonals can contain any duplicated value*.
   This constraint allows the algorithim to discard any candidate value which is already solved in any of the diagonals to which the box belongs.
   In our implementation, horizontal and vertical diagonals are added to the peers set in order to ensure that the peers validation includes them.

## Code
* `solutions.py` - The project solutions can be found here.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

## Visualizing
To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

## Data
The data consists of a text file of diagonal sudokus for you to solve.
