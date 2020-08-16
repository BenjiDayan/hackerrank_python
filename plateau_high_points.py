#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findHighPoints' function below.
#
# The function is expected to return a 2D_BOOLEAN_ARRAY.
# The function accepts 2D_INTEGER_ARRAY elevations as parameter.
#

def findHighPoints(elevations):
    """
6
5
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
1 1 1 1 3
    :param elevations:
    :return:
    """
    # Write your code here
    num_rows = len(elevations)
    num_cols = len(elevations[0])
    num_rows = len(elevations)
    num_cols = len(elevations[0])

    reachable = [[0 for c in range(num_cols)] for r in range(num_rows)]

    neighbour_delta = []
    for delta_r in [-1, 0, 1]:
        for delta_c in [-1, 0, 1]:
            if delta_r == 0 and delta_c == 0:
                continue
            neighbour_delta.append([delta_r, delta_c])

    truth_array = [[True for c in range(num_cols)] for r in range(num_rows)]
    for r in range(num_rows):
        for c in range(num_cols):
            check = True
            element = elevations[r][c]
            for delta_r, delta_c in neighbour_delta:
                new_r = r + delta_r
                new_c = c + delta_c
                print(new_r, new_c)

                if new_r < 0 or new_c < 0 or new_r >= num_rows or new_c >= num_cols:
                    #print('invalid')
                    continue
                if elevations[r + delta_r][c + delta_c] >= element:
                    check = False
                    break

            truth_array[r][c] = check
    return truth_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    elevations_rows = int(input().strip())
    elevations_columns = int(input().strip())

    elevations = []

    for _ in range(elevations_rows):
        elevations.append(list(map(int, input().rstrip().split())))

    result = findHighPoints(elevations)

    fptr.write('\n'.join([' '.join(map(str, map(int, x))) for x in result]))
    fptr.write('\n')

    fptr.close()
