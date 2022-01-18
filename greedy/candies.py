# Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.
# Example
# arr = [4,6,4,5,6,2]
# She gives the students candy in the following minimal amounts: [1,2,1,2,3,1]. She must buy a minimum of 10 candies.

# Function Description
# Complete the candies function in the editor below.
# candies has the following parameter(s):
# - int n: the number of children in the class
# - int arr[n]: the ratings of each student

# Returns
# int: the minimum number of candies Alice must buy

# Input Format
# The first line contains an integer, n, the size of arr.
# Each of the next n lines contains an integer arr[i] indicating the rating of the student at position i.

# Constraints
# 1 ≤ n ≤ 10^5
# 1 ≤ arr[i] ≤ 10^5

# Sample Input 0
#     3
#     1
#     2
#     2

# Sample Output 0
#     4

# Sample Input 1
#     10
#     2
#     4
#     2
#     6
#     1
#     7
#     8
#     9
#     2
#     1

# Sample Output 1
#     19

# Sample Input 2
#     8
#     2
#     4
#     3
#     5
#     2
#     6
#     4
#     5

# Sample Output 2
#     12

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def candies(n: int, arr: list) -> int:
    # Write your code here
    count = [1]*n
    desc_buf = []

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            if not desc_buf:
                desc_buf = [i-1]
            desc_buf.append(i)
            if not i == n-1:
                continue

        if arr[i] > arr[i-1]:
            count[i] = count[i-1] + 1

        if desc_buf:
            for extra, idx in enumerate(desc_buf[::-1]):
                count[idx] = max(count[idx], extra + 1)

            del desc_buf[:]

    return sum(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
