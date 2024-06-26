#!/usr/bin/python3
"""Lock boxes."""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.
        Each box contains a list of integers representing the keys
        that can unlock other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    size = len(boxes)
    checker = {}
    index = 0

    for box in boxes:
        if len(box) == 0 or index == 0:
            checker[index] = -1
            for key in box:
                if key < size and key != index:
                    checker[key] = key
        if len(checker) == size:
            return True
        index += 1

    return False
