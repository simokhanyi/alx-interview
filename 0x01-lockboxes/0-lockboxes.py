#!/usr/bin/env python3
"""
Lockboxes function
"""


def canUnlockAll(boxes):
    def dfs(box_index, keys):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                keys.add(key)
                dfs(key, keys)

    n = len(boxes)
    visited = set()
    keys = {0}  # The first box is always unlocked
    dfs(0, keys)

    return len(keys) == n


# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
