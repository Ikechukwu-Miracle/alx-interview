#!/usr/bin/env python3
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
    # Check if the boxes list is empty
    if not boxes:
        return False
    
    # Initialize variables
    size = len(boxes)
    checker = {}  # Dictionary to keep track of discovered keys
    index = 0  # Index to keep track of current box
    
    # Iterate through each box
    for box in boxes:
        # If the box is empty or it's the first box (index 0), mark it as visited
        if len(box) == 0 or index == 0:
            checker[index] = -1
        # Iterate through keys in the current box
        for key in box:
            # If the key is valid and it's not the same as the current box index
            if key < size and key != index:
                # Store the key in the checker dictionary
                checker[key] = key
        # If all boxes have been discovered, return True
        if len(checker) == size:
            return True
        # Move to the next box
        index += 1
