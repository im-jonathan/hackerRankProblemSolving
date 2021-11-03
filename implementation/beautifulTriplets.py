# Given a sequence of integers a, a triplet(a[i], a[j], a[k]) is beautiful if:
# i < j < k
# a[j] - a[i] = a[k] - a[j] = d
# Given an increasing sequenc of integers and the value of d, count the number of beautiful triplets in the sequence.
# Example
# arr = [2,2,3,4,5]
# d = 1

# There are three beautiful triplets, by index: [i, j, k] = [0, 2, 3], [1, 2, 3], [2, 3, 4]. To test the first triplet, arr[j] - arr[i] = 3 - 2 = 1 and arr[k] - arr[j] = 4 - 3 = 1.

# Function Description
# Complete the beautifulTriplets function in the editor below.

# beautifulTriplets has the following parameters:
# - int d: the value to match
# - int arr[n]: the sequence, sorted ascending

# Returns
# int: the number of beautiful triplets

# Input Format
# The first line contains 2 space-separated integers, n and d, the length of the sequence and the beautiful difference.
# The second line contains n space-separated integers arr[i].

# Constraints
# 1 ≤ n ≤ 10^4
# 1 ≤ d ≤ 20
# 0 ≤ arr[i] ≤ 2x10^4
# arr[i] > arr[i-1]

# Sample Input
#     STDIN           Function
#     ----- --------
#     7 3             arr[] size n = 7, d = 3
#     1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]

# Sample Output
#     3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def beautifulTriplets(d: int, arr: list) -> int:
    # Write your code here
    count = 0
    for item in arr:
        if item+d in arr and item+2*d in arr:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
