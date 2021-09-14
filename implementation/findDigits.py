# An integer d is a divisor of an integer n if the remainder of n%d = 0 .
# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Example
# n = 124
# Check whether 1, 2 and 4 are divisors of 124. All 3 numbers divide evenly into 124 so return 3.
# n = 111
# Check whether , 1, 1 and 1 are divisors of 111. All 3 numbers divide evenly into 111 so return 3.
# n = 10
# Check whether 1 and 0 are divisors of 10. 1 is, but 0 is not. Return 1.

# Function Description
# Complete the findDigits function in the editor below.
# findDigits has the following parameter(s):
# - int n: the value to analyze

# Returns
# int: the number of digits in that are divisors of

# Input Format
# The first line is an integer, t, the number of test cases.
# The t subsequent lines each contain an integer, n.

# Constraints
# 1 ≤ t ≤ 15
# 0 < n < 10^9

# Sample Input
#     2
#     12
#     1012
# Sample Output
#     2
#     3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def findDigits(n: int) -> int:
    # Write your code here
    divisors = 0
    options = map(int, str(n))
    for item in options:
        if item != 0:
            data = n % item
            if data == 0:
                divisors += 1
    return divisors


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
