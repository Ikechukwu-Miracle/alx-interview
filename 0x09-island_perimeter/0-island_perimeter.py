#!/usr/bin/python3
"""Island perimeter algorithm"""


from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """Calculates the peimeter of the Island represented
    as an NxN matrix.
    Args:
        grid (list of list): The grid where the Island exist in
        
    Retuns:
        The total perimeter of the Island
    """
    row = len(grid)
    column = len(grid[0])
    perimeter = 0
    connections = 0
    
    if row > 100 or column > 100:
        return 0
    
    for x in range(row):
        for y in range(column):
            if grid[x][y] == 1:
                perimeter += 4
                
                if x != 0 and grid[x - 1][y] == 1:
                    connections += 1
                if y != 0 and grid[x][y - 1] == 1:
                    connections += 1
                    
    return perimeter - (connections * 2)
    