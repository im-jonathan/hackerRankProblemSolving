# Madam Hannah Otto, the CEO of Reviver Corp., is fond of palindromes, or words that read the same forwards or backwards. She thinks palindromic brand names are appealing to millennials.
# As part of the marketing campaign for the company's new juicer called the Rotator™, Hannah decided to push the marketing team's palindrome-searching skills to a new level with a new challenge.
# In this challenge, Hannah provides a string s consisting of lowercase English letters. Every day, for q days, she would select two integers l and r, take the substring s[l..r] (the substring of s from index l to index r), and ask the following question:
# Consider all the palindromes that can be constructed from some of the letters from s[l..r]. You can reorder the letters as you need. Some of these palindromes have the maximum length among all these palindromes. How many maximum-length palindromes are there?
# For example, if s=madamimadam, l=4 and r=7, then we have,
# s[4:7] = amim, palindromes = mam, mim
# Your job as the head of the marketing team is to answer all the queries. Since the answers can be very large, you are only required to find the answer modulo 10 ^ 9 + 7.
# Complete the functions initialize and answerQuery and return the number of maximum-length palindromes modulo 10^9 + 7.

# Input Format
# The first line contains the string s.
# The second line contains a single integer q.
# The ith of the next q lines contains two space-separated integers li, ri denoting the l and r values Anna selected on the ith day.

# Constraints
# Here, |s| denotes the length of s.
# 1 ≤ |s| ≤ 10^5
# 1 ≤ q ≤ 10^5
# 1 ≤ li ≤ ri ≤ |s|

# Subtasks
# For 30 % of the total score:
# 1 ≤ |s| ≤ 100
# 1 ≤ q ≤ 1000
# li - ri ≤ 3

# For 60 % of the total score:
# 1 ≤ |s| ≤ 100
# 1 ≤ q ≤ 1000

# Output Format
# For each query, print a single line containing a single integer denoting the answer.

# Sample Input 0
#     week
#     2
#     1 4
#     2 3

# Sample Output 0
#     2
#     1

# Sample Input 1
#     abab
#     1
#     1 4

# Sample Output 1
#     2

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from math import factorial

fact = dict()
powr = dict()
dist = defaultdict(lambda: Counter(""))

m = 10 ** 9 + 7


def initialize(s):
    fact[0], powr[0], dist[0] = 1, 1, Counter(s[0])
    for j in range(1, len(s)):
        fact[j] = (j * fact[j - 1]) % m
        dist[j] = dist[j-1] + Counter(s[j])


def power(x, n, m):
    if n == 1:
        return x % m
    elif n % 2 == 0:
        return power(x ** 2 % m, n // 2, m)
    else:
        return (x * power(x ** 2 % m, (n - 1) // 2, m)) % m


def answerQuery(s, l, r):
    # Return the answer for this query modulo 1000000007.
    b = dist[r-1] - dist[l-2]
    p, count, value = 0, 0, 1
    for c in b.values():
        if c >= 2:
            count += c // 2
            value = (value * fact[c // 2]) % m
        if c % 2 == 1:
            p += 1
    return (max(1, p) * fact[count] * power(value, m - 2, m)) % m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    print(dist)
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(s, l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
