# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.
# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String
# Example.
# s = 'aab'
# aab shortens to b in one operation: remove the adjacent a characters.
# s = 'abba'
# Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.

# Function Description
# Complete the superReducedString function in the editor below.
# superReducedString has the following parameter(s):
# - string s: a string to reduce

# Returns
# string: the reduced string or Empty String

# Input Format
# A single string, s.

# Constraints
# 1 ≤ length of s ≤ 100

# Sample Input 0
#     aaabccddd

# Sample Output 0
#     abd

# Sample Input 1
#     aa

# Sample Output 1
#     Empty String

# Sample Input 2
#     baab

# Sample Output 2
#     Empty String


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def superReducedString(s: str) -> str:
    # Write your code here
    letters = list(s)
    i = 0
    while i < len(letters) - 1:
        if letters[i] == letters[i+1]:
            del letters[i+1]
            del letters[i]
            i = 0
            if len(letters) == 0:
                return 'Empty String'
        else:
            i += 1
    return ''.join(letters)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
