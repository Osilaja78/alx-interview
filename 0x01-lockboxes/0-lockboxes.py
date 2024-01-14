#!/usr/bin/python3
"""
Lockboxes solution.
"""


def canUnlockAll(boxes):
    """This method determines if all the boxes can be opened"""

    visited = set()

    def dfs(box):
        visited.add(box)

        for key in boxes[box]:
            if key not in visited and key < len(boxes):
                dfs(key)

    dfs(0)
    return len(visited) == len(boxes)
