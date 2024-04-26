#!/usr/bin/python3
"""
Pascals triangle
"""

def generate_pascal_triangle(num_rows):
    triangle = [[1]]

    for _ in range(1, num_rows):
        row = [1]
        prev_row = triangle[-1]

        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    num_rows = 5
    triangle = generate_pascal_triangle(num_rows)
    print_triangle(triangle)
