#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened or not"""
    if boxes == [] or boxes == [[]] or boxes == [[0]]:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
