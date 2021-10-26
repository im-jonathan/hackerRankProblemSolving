# A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
# Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2xd digits long or (2xd)-1 digits long. Split the string representation of the square into two parts, l and r. The right hand part, r must be l digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n.

# Example
# n = 5
# d = 1
# First calculate that n ^ 2 = 25. Split that into two strings and convert them back to integers 2 and 5. Test 2 + 5 = 7 ≠ 5, so this is not a modified Kaprekar number. If n = 9, still d = 1, and n^2 = 81. This gives us 8 + 1 = 9, the original n.
# Note: r may have leading zeros.

# Given two positive integers p and q where p is lower than q, write a program to print the modified Kaprekar numbers in the range between p and q, inclusive. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE.

# Function Description
# Complete the kaprekarNumbers function in the editor below.

# kaprekarNumbers has the following parameter(s):
# - int p: the lower limit
# - int q: the upper limit

# Prints
# It should print the list of modified Kaprekar numbers, space-separated on one line and in ascending order. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE. No return value is required.

# Input Format
# The first line contains the lower integer limit p.
# The second line contains the upper integer limit q.
# Note: Your range should be inclusive of the limits.

# Constraints
# 0 < p < q < 100000

# Sample Input
#     STDIN   Function
#     ----- --------
#     1       p = 1
#     100     q = 100

# Sample Output
#     1 9 45 55 99

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def kaprekarNumbers(p: int, q: int) -> None:
    # Write your code here
    results = []
    for i in range(p, q+1):
        square = i**2
        d = 10**len(str(i))
        l = square//d
        r = square % d
        if l+r == i:
            results.append(i)
    if results:
        print(*results)
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
