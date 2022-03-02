# Given an array of integers, where all elements but one occur twice, find the unique element.
# Example
# a = [1,2,3,4,3,2,1]
# The unique element is 4.

# Function Description
# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):
# - int a[n]: an array of integers

# Returns
# int: the element that occurs only once

# Input Format
# The first line contains a single integer, n, the number of integers in the array.
# The second line contains n space-separated integers that describe the values in a.

# Constraints
# 1 ≤ n < 100
# It is guaranteed that n is an odd number and that there is one unique element.
# 0 ≤ a[i] ≤ 100, where 0 ≤ i < n.

# Sample Input 0
#     1
#     1

# Sample Output 0
#     1

# Sample Input 1
#     3
#     1 1 2

# Sample Output 1
#     2

# Sample Input 2
#     5
#     0 0 1 2 1

# Sample Output 2
#     2

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a: list) -> int:
    # Write your code here
    data = reduce((lambda x, y: x ^ y), a) # ^ = xor operator
    return data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
