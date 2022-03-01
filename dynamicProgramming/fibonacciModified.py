# Implement a modified Fibonacci sequence using the following definition:
# given terms t[i] and t[i+1] where i ∈ to (1,∞), term t[i+2] is computed as:
#     t[i+2] = t[i] + (t[i]+1)^2
# Given three integers, t1, t2, and n, compute and print the nth term of a modified Fibonacci sequence.
# Example
# t1 = 0
# t2 = 1
# n = 6
# t3 = 0 + 1^2 = 1
# t4 = 1 + 1^2 = 2
# t5 = 1 + 2^2 = 5
# t6 = 2 + 5^2 = 27
# Return 27.

# Function Description
# Complete the fibonacciModified function in the editor below. It must return the nth number in the sequence.
# fibonacciModified has the following parameter(s):
# - int t1: an integer
# - int t2: an integer
# - int n: the iteration to report

# Returns
# int: the nth number in the sequence
# Note: The value of t[n] may far exceed the range of a 64-bit integer. Many submission languages have libraries that can handle such large results but, for those that don't(e.g., C++), you will need to compensate for the size of the result.

# Input Format
# A single line of three space-separated integers, the values of t1, t2, and n.

# Constraints
# 0 ≤ t1,t2 ≤ 2
# 3 ≤ n ≤ 20
# t[n] may far exceed the range of a 64-bit integer.

# Sample Input
#     0 1 5

# Sample Output
#     5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#


def fibonacciModified(t1: int, t2: int, n: int) -> int:
    # Write your code here
    for _ in range(n-1):
        t1, t2 = t2, t1+(t2**2)
    return t1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
