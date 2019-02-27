#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    counter = 0
    for c in s:
        if c == 'a':
            counter = counter + 1
    
    mult = n // len(s)
    remainder = n % len(s)
    counter = counter * mult
    for c in s[:remainder]:
        if c == 'a':
            counter = counter + 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
