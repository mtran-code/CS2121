# Program for playing the game of Life.
from life import LifeGrid

# Define the initial configuration of live cells. 
INIT_CONFIG = [(0, 2), (1, 1), (1, 3), (2, 0), (2, 4), (3, 1), (3, 3), (4, 2)]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 10


def main():
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)


# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    liveCells = list()

    # Iterate over the elements of the grid.
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.isLiveCell(i, j)) or \
                    (neighbors == 3):
                liveCells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(liveCells)


def draw(grid):
    """
    Prints a text-based representation of the game grid.
    :param grid: the game grid to be printed
    :return: None
    """
    # declare empty list to hold all row strings
    complete_data = []

    for x in range(grid.numRows()):
        # declare empty string to represent row
        row_string = ''

        for y in range(grid.numCols()):
            # if cell is alive, add '@' symbol to string
            if grid.isLiveCell(x, y):
                row_string += '@ '

            # if cell is dead, add '.' symbol to string
            else:
                row_string += '. '

        # append the completed row string to the complete list, and continue loop onto next row
        complete_data.append(row_string)

    # print each row in the list separated by a new line
    print('\n'.join(complete_data) + '\n')


# Executes the main routine.  
main()
