#!/bin/python3

import math
import os
import random
import re
import sys

def generate_queue(n):
    """Randomly creates a valid post bribe queue of length n"""
    arr = [x for x in range(1, n+1)]
    moves = arr + arr.copy()
    random.shuffle(moves)
    moves = moves[:random.randint(0, n)]
    print(moves)
    for num2move in moves:
        i = arr.index(num2move)
        if i >= 1:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp
    return arr

# Complete the minimumBribes function below.
# This version is iterative not recursive
def minimumBribes_iterative(q):
    """
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    1, 2, 3,
    """
    length = len(q)
    moves = [0 for i in range(length)]
    moves_made = 0
    arr = q.copy()
    last_pos = length-1
    def get_pos_indices(arr):
        nonlocal last_pos
        while last_pos >= 0 and arr[last_pos] <= last_pos + 1:
            last_pos -= 1

        if last_pos == -1:
            return None
        last_pos += 1 # keep on searching from the one above
        return last_pos - 1
        return last_pos if last_pos >= 0 else None

    while True:
        pos = get_pos_indices(arr)
        if pos is None:
            break
        else:
            thing = arr[pos]
            moves[thing - 1] += 1
            moves_made += 1
            # print(moves_made)
            # print(moves)
            if moves[thing - 1] == 3:
                return -1

            arr = arr[:pos] + [arr[pos + 1]] + [thing] + arr[pos + 2:]

    return moves_made

def minimumBribes(q):
    out = minimumBribes_iterative(q)
    if out == -1:
        print('Too chaotic')
    else:
        print(out)

# Complete the minimumBribes function below.
def minimumBribes_recursive(q):
    """
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    1, 2, 3,
    """
    length = len(q)
    recursion_limit = 2*length + 100
    print(recursion_limit)
    sys.setrecursionlimit(recursion_limit)
    moves = [0 for i in range(length)]
    moves_made = 0
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
            print(moves)
            nonlocal moves_made
            moves_made += 1
            print(moves_made)
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
    # t = int(input())
    #
    # for t_itr in range(t):
    #     n = int(input())
    #
    #     q = list(map(int, input().rstrip().split()))
    #     minimumBribes(q)

    # q = generate_queue(10000)
    # minimumBribes(q)

    q = [1, 2, 5, 3, 4, 6, 9, 8, 10, 7]
    minimumBribes(q)

    # file = open('inputs\\new_year_chaos_input06.txt')
    # t = int(input())
    #
    # for t_itr in range(t):
    #     n = int(input())
    #
    #     q = list(map(int, input().rstrip().split()))