
arr = [-1, 2, -3, 4, 5, -6]
result = [arr[0]]
for x in arr[1:]:
    if (x < 0) != (result[-1] < 0):
        result.append(x)
print(result)

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]

result = max(set(arr), key=arr.count)

print(result)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum =0
    for i in range(len(ar)):
        sum=sum+ar[i]
    return sum

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
