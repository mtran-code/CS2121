# Implements the LifeGrid ADT for use with the game of Life.
from my_array import Array2D


class LifeGrid:
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__(self, numRows, numCols):
        # Allocate the 2-D array for the grid.
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all cells to dead.
        self.configure(list())

        # Returns the number of rows in the grid.

    def numRows(self):
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols(self):
        return self._grid.numCols()

    # Configures the grid to contain the given live cells.
    def configure(self, coordList):
        # Clear the game grid.
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

                # Set the indicated cells to be alive.
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead.
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        """
        determines the number of living cells adjacent (including diagonal) to a given cell
        :param row: row index of given cell
        :param col: column index of given cell
        :return: number of live neighbors for given cell
        """
        # declare empty int counter
        live_neighbor_count = 0

        # check rows and columns within 1 of given cell (i.e. previous row (row-1), same row (row), and next row only (row+1)
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):

                # exclude the cell itself from the neighbor count
                if x_offset == 0 and y_offset == 0:
                    continue

                # only include cells that exist within grid (i.e. row/col index cannot be negative or greater than total row/col number)
                elif 0 <= (row + x_offset) <= (self.numRows() - 1) \
                        and 0 <= (col + y_offset) <= (self.numCols() - 1):

                    # if cell is alive, add one to counter
                    if self.isLiveCell(row + x_offset, col + y_offset):
                        live_neighbor_count += 1

        return live_neighbor_count
