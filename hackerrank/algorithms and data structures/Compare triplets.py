#!binpython3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b)
    #empty results array
    results = []
    #initial scores of 0
    aScore=0
    bScore=0
    
    #loop over the arrays
    for i in range(0,len(a))
        #if a[i]  b[i], a scores a point
        if a[i]  b[i]
            aScore+=1
        #if b[i]  a[i], b scores a point
        elif b[i]  a[i]
            bScore+=1
        #if they are equal no one gets a point
        else
            continue
    #append the points to the results array
    results.append(aScore)
    results.append(bScore)
    return results

if __name__ == '__main__'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('n')

    fptr.close()
