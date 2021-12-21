# A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are 1 to 26 from a to z:
# The weight of a string is the sum of the weights of its characters.
# - A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.
# Given a string,a , let U be the set of weights for all possible uniform contiguous substrings of string s. There will be n queries to answer where each query consists of a single integer. Create a return array where for each query, the value is Yes if query[i] ∈ U. Otherwise, append No.
# Note: The  symbol denotes that x[i] is an element of set U.
# Example
# s = 'abbcccdddd'
# queries = [1,7,5,4,15].
# Working from left to right, weights that exist are:
# string  weight
# a       1
# b       2
# bb      4
# c       3
# cc      6
# ccc     9
# d       4
# dd      8
# ddd     12
# dddd    16
# Now for each value in queries, see if it exists in the possible string weights. The return array is ['Yes', 'No', 'No', 'Yes', 'No'].

# Function Description
# Complete the weightedUniformStrings function in the editor below.
# weightedUniformStrings has the following parameter(s):
# - string s: a string
# - int queries[n]: an array of integers

# Returns
# - string[n]: an array of strings that answer the queries

# Input Format
# The first line contains a string s, the original string.
# The second line contains an integer n, the number of queries.
# Each of the next n lines contains an integer queries[i], the weight of a uniform subtring of s that may or may not exist.

# Constraints
# 1 ≤ length of s, n ≤ 10^5
# 1 ≤ queries[i] ≤ 10^7
# s will only contain lowercase English letters, ascii[a-z].

# Sample Input 0
#     abccddde
#     6
#     1
#     3
#     12
#     5
#     9
#     10

# Sample Output 0
#     Yes
#     Yes
#     Yes
#     Yes
#     No
#     No

# Sample Input 1
#     aaabbbbcccddd
#     5
#     9
#     7
#     8
#     12
#     5

# Sample Output 1
#     Yes
#     No
#     Yes
#     Yes
#     No

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s: str, queries: list) -> list:
    # Write your code here
    a = ord(s[0])-96
    leng = set()
    s = s+"_"
    for i in range(1, len(s)):
        leng.add(a)
        if s[i] == s[i-1]:
            a += (ord(s[i])-96)
        else:
            a = (ord(s[i])-96)
    return ["Yes" if i in leng else "No" for i in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
