#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A 2D list of integers where:
            - 0 represents water
            - 1 represents land

    Returns:
        int: The perimeter of the island.

    Notes:
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn’t have “lakes” (water inside that isn’t connected
          to the water surrounding the island).
        - The grid is rectangular, with its width and height not exceeding 100.
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Directions for checking neighbors: left, right, up, down
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Calculate perimeter for each land cell
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or
                            nc < 0 or nc >= cols or
                            grid[nr][nc] == 0):
                        perimeter += 1

    return perimeter


# Example usage:
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
