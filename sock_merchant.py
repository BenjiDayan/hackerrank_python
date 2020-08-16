#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    print(ar)
    index = 1
    length_ar = len(ar)
    prev_el = ar[0] if length_ar > 0 else None
    groups = [[prev_el, 1]] if prev_el != None else None
    while index < length_ar:
        el = ar[index]
        if el == prev_el:
            groups[-1][1] += 1
        else:
            groups.append([el, 1])
            prev_el = el

        index += 1

    print(groups)
    out = sum([(x[1] // 2) for x in groups])
    print(out)
    return out
    

if __name__ == '__main__':
    print('OUTPUT_PATH={}'.format(os.environ['OUTPUT_PATH']))
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

