# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
# Example
# a = [1,1,2,2,4,4,5,5,5]

# There are two subarrays meeting the criterion: [1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

# Function Description
# Complete the pickingNumbers function in the editor below.
# pickingNumbers has the following parameter(s):
# - int a[n]: an array of integers

# Returns
# int: the length of the longest subarray that meets the criterion

# Input Format
# The first line contains a single integer n, the size of the array a.
# The second line contains n space-separated integers, each an a[i].

# Constraints
# 2 ≤ n ≤ 100
# 0 < a[i] < 100
# The answer will be ≥ 2.

# Sample Input 0
#     6
#     4 6 5 3 3 1

# Sample Output 0
#     3


# Sample Input 1
#     6
#     1 2 2 3 1 2
# Sample Output 1
#     5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a: list) -> int:
    # Write your code here
    maximum = 0
    for item in a:
        count = a.count(item)
        previus_count = a.count(item-1)
        count = count + previus_count
        if count > maximum:
            maximum = count
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
