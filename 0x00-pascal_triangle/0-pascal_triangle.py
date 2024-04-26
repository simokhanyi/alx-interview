#!/usr/bin/python3
"""
Pascals triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal Triangle of n
    Returns an empty list if n <= 0
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    triangle.append([1])

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])

        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal Triangle
    """
    for row in triangle:
        print("[{}]".format(", ".join(map(str, row))))


if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    print_triangle(triangle)
