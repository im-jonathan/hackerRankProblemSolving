# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
# Example
# s = 'The quick brown fox jumps over the lazy dog'
# The string contains all letters in the English alphabet, so return pangram.

# Function Description
# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.
# pangrams has the following parameter(s):
# - string s: a string to test

# Returns
# string: either pangram or not pangram

# Input Format
# A single line with string s.

# Constraints
# 0 length of s ≤ 10^3
# Each character of s, s[i] ∈ {a-z A-Z, space}

# Sample Input
# Sample Input 0
#     We promptly judged antique ivory buckles for the next prize

# Sample Output 0
#     pangram

# Sample Input 1
#     We promptly judged antique ivory buckles for the prize

# Sample Output 1
#     not pangram

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s: str) -> str:
    # Write your code here
    letters = set(s.lower())
    data = ["not pangram", "pangram"][len(letters) == 27]
    return data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
