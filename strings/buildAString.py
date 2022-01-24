# Greg wants to build a string, S of length N. Starting with an empty string, he can perform 2 operations:
# 1. Add a character to the end of S for A dollars.
# 2. Copy any substring of S, and then add it to the end of S for B dollars.
# Calculate minimum amount of money Greg needs to build S.

# Input Format
# The first line contains number of testcases T.
# The 2 x T subsequent lines each describe a test case over 2 lines:
# The first contains 3 space-separated integers, N, A, and B, respectively.
# The second contains S(the string Greg wishes to build).

# Constraints
# 1 ≤ T ≤ 3
# 1 ≤ N ≤ 3x10^4
# 1 ≤ A, B ≤ 10000
# S is composed of lowercase letters only.

# Output Format
# On a single line for each test case, print the minimum cost(as an integer) to build S.

# Sample Input
#     2
#     9 4 5
#     aabaacaba
#     9 8 9
#     bacbacacb

# Sample Output
#     26
#     42

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'buildString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. STRING s
#


def buildString(a: int, b: int, s: str) -> int:
    # Write your code here
    i = 1
    l = len(s)
    cost = 0
    cost = [float('inf')] * (l + 1)
    cost[0] = 0
    k = 0
    while i <= l:
        j = max(i, k)
        while j <= l and (s[i-1:j] in s[:i-1]):
            j += 1

        if j-1 != i:
            cost[j-1] = min(cost[i-1] + b, cost[j-1])
            k = j
        cost[i] = min(cost[i-1] + a, cost[i])
        i += 1

    return cost[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        s = input()

        result = buildString(a, b, s)

        print(result, file=fptr)

    fptr.close()
