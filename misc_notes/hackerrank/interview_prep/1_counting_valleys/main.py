"""
input sample
n = 8
s = UDDDUDUU
"""
def countingValleys(n, s):
    arr = [1 if c == "U" else -1 for c in s]
    total_height = 0
    counter = 0
    for x in arr:
        total_height = total_height + x
        if total_height == 0 and x == 1:
            counter = counter + 1
        
    return counter
