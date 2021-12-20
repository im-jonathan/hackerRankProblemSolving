# We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. Remeber that a subsequence maintains the order of characters selected from a sequence.
# More formally, let p[0], p[1]...p[9] be the respective indices of h, a, c, k, e, r, r, a, n, k in string s. If p[0] < P[1] < p[2] <...< p[9] is true, then  contains hackerrank.
# For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.
# Example
# s = haacckkerrannkk
# This contains a subsequence of all of the characters in the proper order. Answer YES
# s = haacckkerannkk
# This is missing the second 'r'. Answer NO.
# s = hccaakkerrannkk
# There is no 'c' after the first occurrence of an 'a', so answer NO.

# Function Description
# Complete the hackerrankInString function in the editor below.
# hackerrankInString has the following parameter(s):
# - string s: a string

# Returns
# string: YES or NO

# Input Format
# The first line contains an integer q, the number of queries.
# Each of the next q lines contains a single query string s.

# Constraints
# 2 ≤ q ≤ 10^2
# 10 ≤ length of s ≤ 10^4

# Sample Input 0
#     2
#     hereiamstackerrank
#     hackerworld

# Sample Output 0
#     YES
#     NO

# Sample Input 1
#     2
#     hhaacckkekraraannk
#     rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt
# Sample Output 1
#     YES
#     NO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s: str) -> str:
    # Write your code here
    data = (re.search('.*'.join("hackerrank"), s) and "YES") or "NO"
    return data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
