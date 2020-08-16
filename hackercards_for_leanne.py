#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerCards function below.
def hackerCards(collection, d):
    collection = sorted(collection)
    length_collection = len(collection)
    output = []
    money = d
    i = 1
    last_pos = 0
    while True:
        if  last_pos >= length_collection or i < collection[last_pos]:
            if  money >= i:
                output.append(i)
                money -= i
            else:
                break
        else:
            last_pos += 1
        i += 1
    return output

# Complete the hackerCards function below.
def hackerCards1(collection, d):
    collection = sorted(collection)
    output = []
    money = d
    i = 1
    while True:
        if (not i in collection):
            if  money >= i:
                output.append(i)
                money -= i
            else:
                break
        i += 1
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    collection_count = int(input().strip())

    collection = []

    for _ in range(collection_count):
        collection_item = int(input().strip())
        collection.append(collection_item)

    d = int(input().strip())

    res = hackerCards(collection, d)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
