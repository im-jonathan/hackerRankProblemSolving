# Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).
# Insertion Sort and the simple version of Quicksort are stable, but the faster in -place version of Quicksort is not since it scrambles around elements while sorting.
# Design your counting sort to be stable.
# Example
# arr = [[0,'a'],[1,'b'],[0,'c'],[1,'d']]
# The first two strings are replaced with '-'. Since the maximum associated integer is 1, set up a helper array with at least two empty arrays as elements. The following shows the insertions into an array of three empty arrays.

# i	string	converted	list
# 0				        [[], [], []]
# 1 	a       -           [[-], [], []]
# 2	b       -           [[-], [-], []]
# 3	c                   [[-, c], [-], []]
# 4	d                   [[-, c], [-, d], []]
# The result is then printed: - c - d.

# Function Description
# Complete the countSort function in the editor below. It should construct and print the sorted strings.
# countSort has the following parameter(s):
# - string arr[n][2]: each arr[i] is comprised of two strings, x and s

# Returns
# - Print the finished array with each element separated by a single space.
# Note: The first element of each arr[i], x, must be cast as an integer to perform the sort.

# Input Format
# The first line contains n, the number of integer/string pairs in the array arr.
# Each of the next n contains x[i] and s[i], the integers (as strings) with their associated strings.

# Constraints
# 1 ≤ n ≤ 1000000
# n is even
# 1 ≤ |s| ≤ 10
# 1 ≤ x < 100, x ∈ arr
# s[i] consists of characters in the range ascii[a-z]

# Output Format
# Print the strings in their correct order, space-separated on one line.

# Sample Input
#     20
#     0 ab
#     6 cd
#     0 ef
#     6 gh
#     4 ij
#     0 ab
#     6 cd
#     0 ef
#     6 gh
#     0 ij
#     4 that
#     3 be
#     0 to
#     1 be
#     5 question
#     1 or
#     2 not
#     4 is
#     2 to
#     4 the

# Sample Output
#     - - - - - to be or not to be - that is the question - - - -


#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr: list) -> None:
    # Write your code here
    for l in arr:
        l[0] = int(l[0])  # convert first list item to integer

    for i in range(n//2):  # replace first half with hyphen
        arr[i][1] = "-"

    # sort by number into empty list array
    output = [[] for _ in range(n)]
    for l in arr:
        output[l[0]].append(l[1])

    print(' '.join(j for i in output for j in i))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
