#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# sample c = 0 0 0 1 0 0
def jumpingOnClouds(c):
    current_position = 0
    jumps = 0
    while current_position < len(c) - 1:
        if current_position + 2 < len(c):
            if c[current_position + 2] == 0:
                current_position = current_position + 2
                jumps = jumps + 1
            else:
                current_position = current_position + 1
                jumps = jumps + 1
        else:
            if c[current_position + 1] == 0:
                current_position = current_position + 1
                jumps = jumps + 1
    return jumps
        

if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
