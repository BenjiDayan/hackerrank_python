import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    delta_heights = [1 if x == 'U' else -1 for x in list(s)]
    cum_heights = [0]
    for delta in delta_heights:
        cum_heights.append(cum_heights[-1] + delta)

    zero_indices = [i for i in range(len(cum_heights)) if cum_heights[i] == 0]
    is_valley = [cum_heights[index+1] < 0 for index in zero_indices[:-1]]
    print(is_valley)
    return(sum(is_valley))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
