# The factorial of the integer n, written n!, is defined as:
#     n! = n*(n-1)*(n-2)*...*(n-(n+1))

# Calculate and print the factorial of a given integer.
# For example, if n = 30, we calculate 30*29*28*...*2*1 and get 265252859812191058636308480000000.

# Function Description

# Complete the extraLongFactorials function in the editor below. It should print the result and return.
# extraLongFactorials has the following parameter(s):
# - n: an integer
# Note: Factorials of n>20 can't be stored even in a 64 - bit long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.
# We recommend solving this challenge using BigIntegers.

# Input Format
# Input consists of a single integer n

# Constraints
# 1 ≤ n ≤ 100

# Output Format
# Print the factorial of n.

# Sample Input
#     25

# Sample Output
#     5511210043330985984000000

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n: int) -> int:
    # Write your code here
    if n == 1:
        return 1
    prod = n * extraLongFactorials(n-1)
    return prod


if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
