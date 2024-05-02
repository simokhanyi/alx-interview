#!/usr/bin/env python3
"""
Lockboxes function
"""


def canUnlockAll(boxes):
    """
    Function to check if all boxes can be unlocked.
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False

    num_boxes = len(boxes)
    unlocked = {0}  # Start with the first box unlocked

    # Iterate over a copy of the set to avoid modifying it during iteration
    for key in unlocked.copy():
        for box in boxes[key]:
            if 0 <= box < num_boxes and box not in unlocked:
                unlocked.add(box)

    return len(unlocked) == num_boxes


# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
