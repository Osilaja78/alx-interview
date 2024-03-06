#!/usr/bin/python3
"""0-island_perimeter.py module"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a 2D grid"""

    perimeter = 0
    
    # Define directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Iterate through each cell of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell is land
            if grid[i][j] == 1:
                # Check the surrounding cells
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    # Check if the surrounding cell is out of bounds or water
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                        perimeter += 1
    
    return perimeter
