# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
# Example
# s = mom
# The list of all anagrammatic pairs is [m,m][mo,om]at positions [[0],[2]][[0,1],[1,2]] respectively.

# Function Description
# Complete the function sherlockAndAnagrams in the editor below.
# sherlockAndAnagrams has the following parameter(s):
# - string s: a string

# Returns
# int: the number of unordered anagrammatic pairs of substrings in

# Input Format
# The first line contains an integer q, the number of queries.
# Each of the next q lines contains a string s to analyze.

# Constraints
# 1 ≤ q ≤ 10
# 2 ≤ length of s ≤ 100
# s contains only lowercase letters in the range ascii[a-z].

# Sample Input 0
#     2
#     abba
#     abcd

# Sample Output 0
#     4
#     0

# Sample Input 1
#     2
#     ifailuhkqq
#     kkkk

# Sample Output 1
#     3
#     10

# Sample Input 2
#     1
#     cdcd
# Sample Output 2
#     5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s: str) -> int:
    # Write your code here
    anag = 0
    map = {}
    for i in range(len(s)):
        for j in range(len(s) - i):
            s1 = ''.join(sorted(s[j:j + i + 1]))
            map[s1] = map.get(s1, 0) + 1

    for key in map:
        anag += (map[key] - 1) * map[key] // 2

    return anag


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
