# There is a sequence of words in CamelCase as a string of letters, s, having the following properties:
# - It is a concatenation of one or more words consisting of English letters.
# - All letters in the first word are lowercase.
# - For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given s, determine the number of words in s.
# Example
# s = 'oneTwoThree'
# There are 3 words in the string: 'one', 'Two', 'Three'.

# Function Description
# Complete the camelcase function in the editor below.
# camelcase has the following parameter(s):
# - string s: the string to analyze

# Returns
# int: the number of words in

# Input Format
# A single line containing string s.

# Constraints
# 1 ≤ length of s ≤ 10^5

# Sample Input
#     saveChangesInTheEditor

# Sample Output
#     5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def camelcase(s: str) -> int:
    # Write your code here
    uppers = map(str.isupper, s)
    count = sum(uppers) + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
