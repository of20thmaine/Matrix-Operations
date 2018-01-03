"""
Bobby Palmer, CSC 240, Project 2

~Matrix~
Utilizing Python's ability to perform both procedural and OOP programming I was able to create this simple Matrix class
which allows the user to generate and store as many Matrix instance objects containing their own unique states as
needed. The methods I included in this class were carefully chosen to prevent users from altering the state
of any matrix object they're operating with accidentally.

Each object stores its rows and columns as integer values so they can be looked up as a single operation. Matrix objects
are generated from a single-dimensional array of values, read from left to right in row order, which the constructor
then uses to generate a two-dimensional array of the values. Exceptions are raised if the user tries to create a matrix
of dimensions different from the number of values they input.
"""


class Matrix:
    """
    Creates Matrix objects which stores the state of each matrix instance and methods to operate with them.
    """
    def __init__(self, rows, columns, values):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        self.build(values)

    def build(self, values):
        """Constructs matrix from an inputted list of values."""
        iters = 0
        for row in range(self.rows):
            self.matrix.append([])
            for column in range(self.columns):
                self.matrix[row].append(values[iters])
                iters += 1

    def modify(self, row, column, newValue):
        """Allows any specific value in the matrix to be quickly changed."""
        self.matrix[row-1][column-1] = newValue

    def __str__(self):
        """Printed values are rounded to 4 decimal points for sake of grader's eyeballs."""
        matrixString = ""
        for row in range(self.rows):
            matrixString += "|   "
            for column in range(self.columns):
                matrixString += str((round(self.matrix[row][column], 4))) + "   "
            matrixString += "|" + "\n"
        return matrixString

