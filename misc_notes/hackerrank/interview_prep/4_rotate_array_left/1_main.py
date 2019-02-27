#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# time complexity: 0(n)
# space complexity: O(2n)
def rotLeft(a, d):
    rotation = d if len(a) > d else len(a) % d
    temp_arr = []
    for i in range(0, len(a)):
        new_index = (i + rotation) % len(a)
        temp_arr.append(new_index)
    
    arr = []
    for i in range(0, len(a)):
        arr.append(a[temp_arr[i]])
    
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
