#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(arr)
    mask = [[0,0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
    def shift_mask(mask, pos):
        new_mask = [[x[0] + pos[0], x[1] + pos[1]] for x in mask]
        return new_mask

    def get_things(arr, mask):
        elements = []
        for thing in mask:
            elements.append(arr[thing[0]][thing[1]])
        return elements

    def get_shifts(arr):
        return [[x, y] for x in range(len(arr) - 2) for y in range(len(arr[0]) -2)]

    sums = []
    for shift in get_shifts(arr):
        print(shift)
        mask_sum =  sum( get_things(arr, shift_mask(mask, shift)) )
        print(mask_sum)
        sums.append([mask_sum, shift])

    out, max_shift = max(sums, key=lambda x: x[0])
    print("max: {} at index: {}".format(out, max_shift))
    return out

def combine_2_iterables(iter1, iter2):
    for x1 in iter1:
        for x2 in iter2:
            yield [x1, x2]

def combine_multiple_iterables(*iterables):
    combined_iter = reduce(lambda iter1, iter2: combine_2_iterables(iter1, iter2), iterables)
    for element in combined_iter:
        if len(element) > 2:
            yield reduce(lambda left, right: left + [right],  element)
        else:
            yield element

if __name__ == '__main__':
    # Sample input
    """
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
