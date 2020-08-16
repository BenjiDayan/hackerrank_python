#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
from functools import reduce

# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr = np.array(arr)
    print(arr)
    mask = np.array([[1,1,1],[0, 1, 0], [1, 1, 1]])
    print(mask)
    assert len(arr.shape) == len(mask.shape), "mask and array should have same number of dimensions"
    search_limits = np.array(arr.shape) - np.array(mask.shape)
    assert not np.any(search_limits < 0), "mask shape is larger than array shape in some dimension"

    mask_sums = np.zeros(shape = search_limits+1).astype(int)
    for mask_position in combine_multiple_iterables(*[range(limit+1) for limit in search_limits]):
        print(mask_position)
        foo = np.sum(arr[tuple([slice(mask_position[i], mask_position[i] + mask.shape[i]) for i in range(len(mask.shape))])])
        print(foo)
        mask_sums[tuple(mask_position)] = foo

    max, argmax = np.max(mask_sums), np.unravel_index(np.argmax(mask_sums), mask_sums.shape)
    print("max: {} at index: {}".format(max, argmax))
    return max

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
