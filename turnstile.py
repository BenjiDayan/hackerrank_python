#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTimes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY time
#  2. INTEGER_ARRAY direction
#

def getTimes2(time, direction):
    # Write your code here
    inflow = [time[i] for i in range(len(time)) if direction[i] == 0]
    inflow.reverse()
    outflow = [time[i] for i in range(len(time)) if direction[i] == 1]
    outflow.reverse()

    output = []
    t = 0
    last_use = -1
    while len(inflow) > 0 or len(outflow) > 0:
        last_use = get_use(inflow, outflow, t, last_use)
        if last_use == 1:
            outflow.pop()
            output.append([1, t])
        if last_use == 0:
            inflow.pop()
            output.append([0, t])
        t += 1

    new_output = []
    in_times, out_times = [x[1] for x in output if x[0] == 0], [x[1] for x in output if x[0] == 1]
    in_times.reverse()
    out_times.reverse()
    temp = [in_times, out_times]
    for i, d in enumerate(direction):
        new_output.append(temp[d].pop())

    return new_output

def getTimes(time, direction):
    # Write your code here
    inflow = [time[i] for i in range(len(time)) if direction[i] == 0]
    #inflow.reverse()
    outflow = [time[i] for i in range(len(time)) if direction[i] == 1]
    #outflow.reverse()

    li, lo = len(inflow), len(outflow)
    in_index, out_index = 0, 0

    output = []
    t = 0
    last_use = -1
    while in_index < li or out_index < lo:
        last_use = get_use(inflow, outflow, in_index, out_index, li, lo, t, last_use)
        if last_use == 1:
            output.append([1, t])
            out_index += 1
        if last_use == 0:
            output.append([0, t])
            in_index += 1
        t += 1

    new_output = []
    in_times, out_times = [x[1] for x in output if x[0] == 0], [x[1] for x in output if x[0] == 1]
    in_times.reverse()
    out_times.reverse()
    temp = [in_times, out_times]
    for i, d in enumerate(direction):
        new_output.append(temp[d].pop())

    return new_output

def get_use(inflow, outflow, in_index, out_index, li, lo, t, last_use):
    # last_use in 0, 1, -1 (-1 for not used in last second
    if in_index < li:
        in_time = inflow[in_index]
    else:
        in_time = int(1e11)

    if out_index < lo:
        out_time = outflow[out_index]
    else:
        out_time = int(1e11)
    #in_time, out_time = inflow[-1], outflow[-1]

    if in_time <= t and out_time <= t:
        if last_use in [0, 1]:
            return last_use
        else:
            return 1
    elif out_time <= t:
        return 1
    elif in_time <= t:
        return 0
    else:
        return -1

def generate_x(n):
    stuff = [i for i in range(n)], [i for i in range(n)]
    a, b = [], []
    for x in stuff:
        if random.randint(0, 1):
            a.append(x)
        if random.randint(0, 1):
            b.append(x)

    return [a, b]

def generate_stuff(n):
    stuff = [i for i in range(n)]
    a, b = [], []
    for x in stuff:
        if random.randint(0, 1):
            a.append(x)
            b.append(0)
        if random.randint(0, 1):
            a.append(x)
            b.append(1)

    return a, b

if __name__ == '__main__':
    time, direction = generate_stuff(int(1e6))
    result = getTimes(time, direction)
    print(result)

