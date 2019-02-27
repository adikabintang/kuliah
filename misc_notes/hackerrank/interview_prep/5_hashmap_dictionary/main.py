#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazineDict = {}
    for m in magazine:
        if m in magazineDict.keys():
            magazineDict[m] = magazineDict[m] + 1
        else:
            magazineDict[m] = 1
    
    for n in note:
        if n in magazineDict.keys():
            if magazineDict[n] == 1:
                magazineDict.pop(n)
            else:
                magazineDict[n] = magazineDict[n] - 1
        else:
            print("No")
            return
    
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
