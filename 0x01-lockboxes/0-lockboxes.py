#!/usr/bin/python3
"""LOCKED BOXES"""


def canUnlockAll(boxes):
    """
    take the boxes and
        create a set of keys
            go to box[0]
                get all keys and add them setofkeys
            start opening boxes from setofkeys
                go to each box of each key
                    and take the keys from it and add them to set of keys
                keep loping through all setof keys
            ignore keys that dont have box
            track opening of boxes by a counter, if at end it
            equal to lentgh of boxes it mean all boxes unlock
            OPTIMIZE IDEA :
                if we add 0 to setofkeys at start, we dont need for in 23
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for keyy in boxes[setkey]:
            if 0 < keyy < total_boxes and keyy not in setofkeys:
                setofkeys.append(keyy)
                counter += 1
        index += 1

    return counter == total_boxes - 1
