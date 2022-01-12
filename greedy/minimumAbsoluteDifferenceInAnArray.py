# The absolute difference is the positive difference between two values a and b, is written |a-b| or |b-a| and they are equal. If a=3 and b=2, |3-2|=|2-3|=1. Given an array of integers, find the minimum absolute difference between any two elements in the array.
# Example.
# arr = [-2,2,4]
# There are 3 pairs of numbers: [-2,2],[-2,4] and [2,4]. The absolute differences for these pairs are |(-2)-2|=4, |(-2)-4|=6 and |2-4|=2. The minimum absolute difference is 2.

# Function Description
# Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.
# minimumAbsoluteDifference has the following parameter(s):
# int arr[n]: an array of integers

# Returns
# int: the minimum absolute difference found

# Input Format
# The first line contains a single integer n, the size of arr.
# The second line contains n space-separated integers, arr[i].

# Constraints
# 2 ≤ n ≤ 10^5
# -10^9 ≤ arr[i] ≤ 10^9

# Sample Input 0
#     3
#     3 - 7 0

# Sample Output 0
#     3

# Sample Input 1
#     10
#     -59 - 36 - 13 1 - 53 - 92 - 2 - 96 - 54 75

# Sample Output 1
#     1
    
# Sample Input 2
#     5
#     1 - 3 71 68 17

# Sample Output 2
#     3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumAbsoluteDifference(arr: list) -> int:
    # Write your code here
    least = max(max(arr), min(arr) * -1) * 2
    arr = sorted(arr)
    for i in range(0, math.ceil(len(arr) / 2)):
        f = abs(arr[i] - arr[i + 1])
        b = abs(arr[-(i + 1)] - arr[-(i + 2)])
        if (least > min(f, b)):
            least = min(f, b)

            if (least == 0):
                return 0

    return least


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
