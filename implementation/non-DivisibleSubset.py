# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S' is not evenly divisible by k.

# Example
# S = [19,10,12,10,24,25,22] k = 4
# One of the arrays that can be created is S'[0] = [10,12,25]. Another is S'[1] = [19,22,24]. After testing all permutations, the maximum length solution array has 3 elements.

# Function Description
# Complete the nonDivisibleSubset function in the editor below.
# nonDivisibleSubset has the following parameter(s):
# - int S[n]: an array of integers
# - int k: the divisor

# Returns
# int: the length of the longest subset of  meeting the criteria

# Input Format
# The first line contains 2 space-separated integers, n and k, the number of values in S and the non factor.
# The second line contains n space-separated integers, each an S[i], the unique values of the set.

# Constraints
# 1 ≤ n ≤ 10^5
# 1 ≤ k ≤ 100
# 1 ≤ S[i] ≤ 10^9
# All of the given numbers are distinct.

# Sample Input
#     STDIN    Function
#     ----- --------
#     4 3      S[] size n = 4, k = 3
#     1 7 2 4  S = [1, 7, 2, 4]

# Sample Output
#     3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k: int, s: list) -> int:
    # Write your code here
    res = [0 for i in range(0, k)]
    for i in s:
        res[i % k] += 1
    maxN = 1 if res[0] > 0 else 0
    for i in range(1, k//2+1):
        if (i != k-i):
            maxN += max(res[i], res[k-i])
        else:
            maxN += 1
    return maxN


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
