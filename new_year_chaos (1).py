#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    """
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    1, 2, 3,
    """
    length = len(q)
    moves = [0 for i in range(length)]
    def get_pos_indices(arr):
        for i2 in range(length-1, -1, -1):
            if arr[i2] > i2 + 1:
                return i2

        return None

    def idk(arr):
        pos = get_pos_indices(arr)
        if pos is None:
            return 0
        else:
            thing = arr[pos]
            moves[thing-1] += 1
            if moves[thing-1] == 3:
                return -1
            else:
                new_min = idk(arr[:pos] + [arr[pos+1]] + [thing] + arr[pos+2:])
                if new_min == -1:
                    return -1
                else:
                    return 1 + new_min

    out =  idk(q)
    if out == -1:
        print('Too chaotic')
    else:
        print(out)




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)