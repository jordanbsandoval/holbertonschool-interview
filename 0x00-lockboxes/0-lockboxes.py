#!/usr/bin/python3
"""Lock boxes"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    list_keys = boxes[0]
    box_locked = [False] + [True] * (num_boxes - 1)
    for key in list_keys:
        if ((key < num_boxes) and (box_locked[key] is True)):
            box_locked[key] = False
            list_keys.extend(boxes[key])
    return not any(box_locked)
