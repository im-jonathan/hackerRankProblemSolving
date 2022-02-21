# There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that the relation A'[i]+B'[i] ≥ k holds for all i where 0 ≤ i < n.
# There will be q queries consisting of, A, B and k. For each query, return YES if some permutation A', B' satisfying the relation exists. Otherwise, return NO.
# Example
# A = [0,1]
# B = [0,2]
# k = 1
# A valid A', B' is A' = [0, 1] and B' = [2, 0]: 1+0≥1 and 0+2≥1. Return YES.

# Function Description
# Complete the twoArrays function in the editor below. It should return a string, either YES or NO.
# twoArrays has the following parameter(s):
# - int k: an integer
# - int A[n]: an array of integers
# - int B[n]: an array of integers

# Returns
# - string: either YES or NO

# Input Format
# The first line contains an integer q, the number of queries.
# The next q sets of w lines are as follows:
# - The first line contains two space-separated integers n and k, the size of both arrays A and B, and the relation variable.
# - The second line contains n space-separated integers A[i].
# - The third line contains  space-separated integers B[i].

# Constraints
# 1 ≤ q ≤ 10
# 1 ≤ n ≤ 1000
# 1 ≤ k ≤ 10^9
# 0 ≤ A,B ≤ 10^9

# Sample Input
#     STDIN       Function
#     ----- --------
#     2           q = 2
#     3 10        A[] and B[] size n = 3, k = 10
#     2 1 3       A = [2, 1, 3]
#     7 8 9       B = [7, 8, 9]
#     4 5         A[] and B[] size n = 4, k = 5
#     1 2 2 1     A = [1, 2, 2, 1]
#     3 3 3 4     B = [3, 3, 3, 4]

# Sample Output
#     YES
#     NO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def twoArrays(k: int, A: list, B: list) -> str:
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    for item in enumerate(A):
        if A[item[0]] + B[item[0]] < k:
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
