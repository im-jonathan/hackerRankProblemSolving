# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
# Example
# s1 = 'ABCD'
# s2 = 'ABDC'
# These strings have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Return 3.

# Function Description
# Complete the commonChild function in the editor below.
# commonChild has the following parameter(s):
# - string s1: a string
# - string s2: another string

# Returns
# int: the length of the longest string which is a common child of the input strings

# Input Format
# There are two lines, each with a string, s1 and s2.

# Constraints
# 1 ≤ |s1|, |s2| ≤ 5000 where |s| means "the length of "
# All characters are upper case in the range ascii[A-Z].

# Sample Input
#     HARRY
#     SALLY

# Sample Output
#     2

# Sample Input 1
#     AA
#     BB

# Sample Output 1
#     0

# Sample Input 2
#     SHINCHAN
#     NOHARAAA

# Sample Output 2
#     3

# Sample Input 3
#     ABCDEF
#     FBDAMN
# Sample Output 3
#     2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def commonChild(s1: str, s2: str) -> int:
    # Write your code here
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
