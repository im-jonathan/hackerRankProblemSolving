# The distance between two array values is the number of indices between them. Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, return -1.

# Example
# a = [3,2,1,2,3]
# There are two matching pairs of values: 2 and 3. The indices of the 3's are i=0 and j=4, so their distance is d[i,j] = |j-i| = 4. The indices of the 2's are i = 1 and j = 3, so their distance is d[i,j] = |j-i| = 2. The minimum distance is 2.

# Function Description
# Complete the minimumDistances function in the editor below.

# minimumDistances has the following parameter(s):
# - int a[n]: an array of integers

# Returns
# - int: the minimum distance found or -1 if there are no matching elements

# Input Format
# The first line contains an integer n, the size of array a.
# The second line contains n space-separated integers a[i].

# Constraints
# 1 ≤ n ≤ 10^3
# 1 ≤ a[i] ≤ 10^5

# Output Format
# Print a single integer denoting the minimum d[i,j] in a. If no such value exists, print -1.

# Sample Input
#     STDIN           Function
#     ----- --------
#     6               arr[] size n = 6
#     7 1 3 4 1 7     arr = [7, 1, 3, 4, 1, 7]

# Sample Output
#     3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def minimumDistances(a: list) -> int:
    # Write your code here
    result = []
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.append(abs(j-i))
    if result:
        return min(result)
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
