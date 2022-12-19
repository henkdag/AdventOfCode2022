from utilities import *
import numpy as np

data = GetData(2022, 8)

#Turn list of lists into grid
grid = np.array([list(line.strip()) for line in data], int)
#Make grid of zeroes with same dimensions
sumgrid = np.zeros_like(grid, int)
multiplygrid = np.ones_like(grid, int)

#For every side of the grid
for rotation in range(4):
    #For every coordinate in the grid
    for x, y in np.ndindex(grid.shape):
        #For every next number in row, if next number in row is bigger then current, true 
        lower = [num < grid[x, y] for num in grid[x, y+1:]]
        #If value in lower == True, set 1 on grid of zeroes
        sumgrid[x, y] |= all(lower)

        multiplygrid[x, y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))
        #Rotate grid
        grid, sumgrid, multiplygrid = map(np.rot90, [grid, sumgrid, multiplygrid])

print(sumgrid.sum(), multiplygrid.max())