# Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.
# But, to lock the door he needs a key that is an anagram of a palindrome. He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome. Given a string, determine if it can be rearranged into a palindrome. Return the string YES or NO.
# Example
# s = 'aabbccdd'
# One way this can be arranged into a palindrome is abcddcba. Return YES.

# Function Description
# Complete the gameOfThrones function below.
# gameOfThrones has the following parameter(s):
# - string s: a string to analyze

# Returns
# string: either YES or NO

# Input Format
# A single line which contains s.

# Constraints
# 1 ≤ |s| ≤ 10^5
# s contains only lowercase letters in the range ascii[a-z]

# Sample Input 0
#     aaabbbb

# Sample Output 0
#     YES

# Sample Input 1
#     cdefghmnopqrstuvw

# Sample Output 1
#     NO

# Sample Input 2
#     cdcdcdcdeeeef

# Sample Output 2
#     YES

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def gameOfThrones(s: str) -> str:
    # Write your code here
    a = Counter(s)
    b = 0
    for i, j in a.items():
        if j % 2 != 0:
            b += 1
    if b <= 1:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
