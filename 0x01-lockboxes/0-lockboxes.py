#!/usr/bin/env python3
"""
Lockboxes function
"""


def canUnlockAll(boxes):
    """
    Determines whether all locked boxes can be opened based on the keys
    available.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    num_boxes = len(boxes)

    for key in range(1, num_boxes):
        box_checked = False
        for idx in range(num_boxes):
            if key in boxes[idx] and key != idx:
                box_checked = True
                break
        if not box_checked:
            return False

    return True
