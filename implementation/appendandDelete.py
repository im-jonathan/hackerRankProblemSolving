# You have two strings of lowercase English letters. You can perform two types of operations on the first string:
# 1. Append a lowercase English letter to the end of the string.
# 2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on . If it's possible, print Yes. Otherwise, print No.
# Example. s = [a,b,c]
# t = [d,e,f]
# k = 6
# To convert s to t, we first delete all of the characters in 3 moves. Next we add each of the characters of t in order. On the 6th move, you will have the matching string. Return Yes.
# If there were more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than 6 moves, we would not have succeeded in creating the new string.

# Function Description
# Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

# appendAndDelete has the following parameter(s):
# - string s: the initial string
# - string t: the desired string
# - int k: the exact number of operations that must be performed

# Returns
# string: either Yes or No

# Input Format
# The first line contains a string s, the initial string.
# The second line contains a string t, the desired final string.
# The third line contains an integer k, the number of operations.

# Constraints
# 1 ≤ |s| ≤ 100
# 1 ≤ |t| ≤ 100
# 1 ≤ |k| ≤ 100
# s and t consist of lowercase English letters, ascii[a-z].

# Sample Input 0
#     hackerhappy
#     hackerrank
#     9

# Sample Output 0
#     Yes

# Sample Input 1
#     aba
#     aba
#     7

# Sample Output 1
#     Yes

# Sample Input 2
#     ashley
#     ash
#     2

# Sample Output 2
#     No

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s: str, t: str, k: int) -> str:
    # Write your code here
    numSameChars = min(len(s), len(t))
    for i in range(len(t)):
        if s[:i] != t[:i]:
            numSameChars = i-1
            break

    diff = len(s)-numSameChars + len(t)-numSameChars
    result = 'Yes' if (diff <= k and diff % 2 == k %
                       2) or len(s) + len(t) < k else 'No'
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
