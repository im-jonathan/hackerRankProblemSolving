# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
# Example
# s = 'bcbc'
# Either remove 'b' at index 0 or 'c' at index 3.

# Function Description
# Complete the palindromeIndex function in the editor below.
# palindromeIndex has the following parameter(s):
# - string s: a string to analyze

# Returns
# int: the index of the character to remove or

# Input Format
# The first line contains an integer q, the number of queries.
# Each of the next q lines contains a query string s.

# Constraints
# 1 ≤ q ≤ 20
# 1 ≤ length of s ≤ 10^5 + 5
# All characters are in the range ascii[a-z].

# Sample Input
#     STDIN   Function
#     ----- --------
#     3       q = 3
#     aaab    s = 'aaab' (first query)
#     baa     s = 'baa'  (second query)
#     aaa     s = 'aaa'  (third query)

# Sample Output
#     3
#     0
#     -1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromeIndex(s: str) -> int:
    # Write your code here
    if s == s[::-1]:
        return -1
    a = list(s)
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            a.pop(i)
            if a == a[::-1]:
                return i
            else:
                return (len(a)-i)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
