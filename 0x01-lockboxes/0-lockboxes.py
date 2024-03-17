#!/usr/bin/env python3
"""
Lock boxes.
"""


def canUnlockAll(boxes):
    """Checks for unlocked boxes"""
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
