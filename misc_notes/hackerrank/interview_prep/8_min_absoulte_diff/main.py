#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
# Result: timeout, O(n**2)
def minimumAbsoluteDifference(arr):
    min_diff = abs(arr[1] - arr[0])
    for i in range(0, len(arr) - 1):
        for j in range(i+1, len(arr)):
            diff = abs(arr[j] - arr[i])
            if diff < min_diff:
                min_diff = diff
    
    return min_diff

# Result: true. Probably O(n * log(n)), since sort in python is O(n * log(n))
def minimumAbsoluteDifferenceWithSort(arr):
    arr.sort()
    min_diff = abs(arr[1] - arr[0])

    for i in range(0, len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
    
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
