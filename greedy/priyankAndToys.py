# Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. All items meeting that requirement will be shipped in one container.
# What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?
# For example, there are items with weights w=[1,2,3,4,5,10,11,12,13]. This can be broken into two containers: [1,2,3,4,5] and [10,11,12,13]. Each container will contain items weighing within 4 units of the minimum weight item.

# Function Description
# Complete the toys function in the editor below. It should return the minimum number of containers required to ship.
# toys has the following parameter(s):
# - w: an array of integers that represent the weights of each order to ship

# Input Format
# The first line contains an integer n, the number of orders to ship.
# The next line contains n space-separated integers, w[1],w[2],...,w[n], representing the orders in a weight array.

# Constraints
# 1 ≤ n ≤ 10^5
# 0 ≤ w[i] ≤ 10^4, where i ∈ [1,n]

# Output Format
# Return the integer value of the number of containers Priyanka must contract to ship all of the toys.

# Sample Input
#     8
#     1 2 3 21 7 12 14 21

# Sample Output
#     4

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#


def toys(w: list) -> int:
    # Write your code here
    i = 0
    w = set(w)
    while len(w) > 0:
        i += 1
        m = min(w)
        w = w.difference(set(range(m, m + 5)))

    return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
