
# Function Description
# Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.
# countApplesAndOranges has the following parameter(s):
# - s: integer, starting point of Sam's house location.
# - t: integer, ending location of Sam's house location.
# - a: integer, location of the Apple tree.
# - b: integer, location of the Orange tree.
# - apples: integer array, distances at which each apple falls from the tree.
# - oranges: integer array, distances at which each orange falls from the tree.

# Input Format
# The first line contains two space-separated integers denoting the respective values of s and t.
# The second line contains two space-separated integers denoting the respective values of a and b.
# The third line contains two space-separated integers denoting the respective values of m and n.
# The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
# The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

# Constraints
# 1 ≤ s, t, a, b, m, n ≤ 10^5
# -10^5 ≤ d ≤ 10^5
# a < s < t < b

# Output Format
# Print two integers on two different lines:
# The first integer: the number of apples that fall on Sam's house.
# The second integer: the number of oranges that fall on Sam's house.

# Sample Input 0
#     7 11
#     5 15
#     3 2
#     -2 2 1
#     5 -6

# Sample Output 0
#     1
#     1

# Explanation 0
# The first apple falls at position 5-2=3.
# The second apple falls at position 5+2=7.
# The third apple falls at position 5+1=6.
# The first orange falls at position 15+5=20.
# The second orange falls at position 15-6=9.
# Only one fruit (the second apple) falls within the region between 7 and 11, so we print 1 as our first line of output.
# Only the second orange falls within the region between 7 and 11, so we print 1 as our second line of output.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    total_apples = 0
    total_oranges = 0

    for apple in apples:
        location = a + apple
        if location >= s and location <= t:
            total_apples += 1

    for orange in oranges:
        location = b + orange
        if location >= s and location <= t:
            total_oranges += 1

    print(total_apples)
    print(total_oranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
