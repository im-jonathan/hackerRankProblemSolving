# Two words are anagrams of one another if their letters can be rearranged to form the other word.
# Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.
# Example
# s = abccde
# Break s into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

# Function Description
# Complete the anagram function in the editor below.
# anagram has the following parameter(s):
# - string s: a string

# Returns
# - int: the minimum number of characters to change or -1.

# Input Format
# The first line will contain an integer, q, the number of test cases.
# Each test case will contain a string s.

# Constraints
# 1 ≤ q ≤ 100
# 1 ≤ |s| ≤ 10^4
# s consists only of characters in the range ascii[a-z].

# Sample Input
#     6
#     aaabbb
#     ab
#     abc
#     mnop
#     xyyx
#     xaxbbbxx

# Sample Output
#     3
#     1
#     -1
#     2
#     0
#     1

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def anagram(s: str) -> int:
    # Write your code here
    l = len(s)
    if l % 2:
        return -1
    l = l//2
    a = Counter(s[:l])
    b = Counter(s[l:])
    data = l - sum((a & b).values())
    return data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
