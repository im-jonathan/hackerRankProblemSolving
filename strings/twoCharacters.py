# Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.
# Example
# s = 'abaacdabd'
# Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at any point would not result in a valid string. Return 4.
# Given a string s, convert it to the longest possible string t made up only of alternating characters. Return the length of string t. If no string t can be formed, return 0.

# Function Description
# Complete the alternate function in the editor below.
# alternate has the following parameter(s):
# - string s: a string

# Returns.
# int: the length of the longest valid string, or if there are none

# Input Format
# The first line contains a single integer that denotes the length of .
# The second line contains string s.

# Constraints
# 1 ≤ length of s ≤ 1000
# s[i] ∈ ascii[a-z]

# Sample Input
#     STDIN       Function
#     ----- --------
#     10          length of s = 10
#     beabeefeab  s = 'beabeefeab'

# Sample Output
#     5

# Explanation
# The characters present in s are a, b, e, and f. This means that t must consist of two of those characters and we must delete two others. Our choices for characters to leave are[a, b], [a, e], [a, f], [b, e], [b, f] and [e, f].
# If we delete e and f, the resulting string is babab. This is a valid t as there are only two distinct characters(a and b), and they are alternating within the string.
# If we delete a and f, the resulting string is bebeeeb. This is not a valid string t because there are consecutive e's present. Removing them would leave consecutive b's, so this fails to produce a valid string t.
# Other cases are solved similarly.
# babab is the longest string we can create.

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternate(s: str) -> int:
    # Write your code here
    x = set(s)
    m = 0
    l = list(map(set, combinations(x, 2)))
    for i in l:
        y = x-i
        z = s
        for j in y:
            z = z.replace(j, "")
        r = ("".join(i))*(len(z)//2)
        if r+r[0] == z or r == z or r == z[::-1] or r[1]+r == z:
            m = max(m, len(z))
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
