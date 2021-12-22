# A numeric string,s, is beautiful if it can be split into a sequence of two or more positive integers, a[1],a[2],...,a[n], satisfying the following conditions:
# a[i] - a[i-1] = 1 for any 1 < i ≤ n (i.e., each element in the sequence is 1 more than the previous element).
# No a[i] contains a leading zero. For example, we can split s = 10203 into the sequence {1,02,03}, but it is not beautiful because 02 and 03 have leading zeroes.
# The contents of the sequence cannot be rearranged. For example, we can split s = 321 into the sequence {3, 2, 1}, but it is not beautiful because it breaks our first constraint(i.e., 1-3≠1).
# Perform q queries where each query consists of some integer string s. For each query, print whether or not the string is beautiful on a new line. If it is beautiful, print YES x, where x is the first number of the increasing sequence. If there are multiple such values of x, choose the smallest. Otherwise, print NO.

# Function Description
# Complete the separateNumbers function in the editor below.
# separateNumbers has the following parameter:
# - s: an integer value represented as a string

# Prints
# - string: Print a string as described above. Return nothing.

# Input Format
# The first line contains an integer q, the number of strings to evaluate.
# Each of the next q lines contains an integer string s to query.

# Constraints
# 1 ≤ q ≤ 10
# 1 ≤ |s| ≤ 32
# s[i] ∈ [0-9]

# Sample Input 0
#     7
#     1234
#     91011
#     99100
#     101103
#     010203
#     13
#     1

# Sample Output 0
#     YES 1
#     YES 9
#     YES 99
#     NO
#     NO
#     NO
#     NO

# Sample Input 1
#     4
#     99910001001
#     7891011
#     9899100
#     999100010001

# Sample Output 1
#     YES 999
#     YES 7
#     YES 98
#     NO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s: str) -> None:
    # Write your code here
    found = False
    for i in range(len(s)//2):
        a = s[:i+1]
        f = n = int(s[:i+1])
        while len(a) < len(s):
            n += 1
            a += str(n)
        if a == s:
            found = True
            print(f'YES {f}')
            break
    if not found:
        print('NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
