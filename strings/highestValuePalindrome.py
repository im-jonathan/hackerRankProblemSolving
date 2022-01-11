# Palindromes are strings that read the same from the left or right, for example madam or 0110.
# You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 0's left of all higher digits in your tests. For example 0110 is valid, 0011 is not.
# Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.
# Example
# s = '1231'
# k = 3
# Make 3 replacements to get '9339'.
# s = '12321'
# k = 1
# Make  replacement to get 12921.

# Function Description
# Complete the highestValuePalindrome function in the editor below.
# highestValuePalindrome has the following parameter(s):
# - string s: a string representation of an integer
# - int n: the length of the integer string
# - int k: the maximum number of changes allowed

# Returns
# string: a string representation of the highest value achievable or -1

# Input Format
# The first line contains two space-separated integers, n and k, the number of digits in the number and the maximum number of changes allowed.
# The second line contains an n-digit string of numbers.

# Constraints
# 0 < n ≤ 10^5
# 0 ≤ k ≤ 10^5
# Each character in the number is an integer where 0 ≤ i ≤ 9.

# Output Format
# Sample Input 0
#     STDIN   Function
#     ----- --------
#     4 1     n = 4, k = 1
#     3943    s = '3943'

# Sample Output 0
#     3993

# Sample Input 1
#     6 3
#     092282

# Sample Output 1
#     992299

# Sample Input 2
#     4 1
#     0011
    
# Sample Output 2
#     -1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#


def highestValuePalindrome(s: str, n: int, k: int) -> str:
    # Write your code here
    s = list(s)
    count = 0
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            count += 1
    if count > k:
        return '-1'
    if k >= n:
        return '9'*n

    count = k-count
    for i in range(n//2):
        if s[i] != s[n-1-i] and count != 0:
            if s[i] != '9' and s[n-1-i] != '9':
                count = count-1
            s[i] = s[n-i-1] = '9'
        elif s[i] != s[n-1-i] and count == 0:
            s[i] = s[n-i-1] = max(s[i], s[n-i-1])
        elif s[i] == s[n-1-i] and count > 1 and s[i] != '9':
            count -= 2
            s[i] = s[n-1-i] = '9'
        else:
            continue
    if count > 0 and n % 2 == 1:
        s[n//2] = '9'
    return ''.join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
