# A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1. The first flower will be original price, (0+1)*original price, the next will be(1+1)*original price and so on.
# Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers. The number of flowers they want equals the length of the c array.
# Example
# c = [1,2,3,4]
# k = 3
# The length of c=4, so they want to buy 4 flowers total. Each will buy one of the flowers priced [2,3,4] at the original price. Having each purchased x=1 flower, the first flower in the list, c[0], will now cost (current purchase + previous purchase)*c[0] = (1+1)*1 = 2. The total cost is 2+3+4+2=11.

# Function Description
# Complete the getMinimumCost function in the editor below.
# getMinimumCost has the following parameter(s):
# - int c[n]: the original price of each flower
# - int k: the number of friends

# Returns
# - int: the minimum cost to purchase all flowers

# Input Format
# The first line contains two space-separated integers n and k, the number of flowers and the number of friends.
# The second line contains n space-separated positive integers c[i], the original price of each flower.

# Constraints
# 1 ≤ n,k ≤ 100
# 1 ≤ c[i] ≤ 10^6
# answer < 2^31
# 0 ≤ i < n

# Sample Input 0
#     3 3
#     2 5 6

# Sample Output 0
#     13

# Sample Input 1
#     3 2
#     2 5 6

# Sample Output 1
#     15

# Sample Input 2
#     5 3
#     1 3 5 7 9

# Sample Output 2
#     29

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


def getMinimumCost(k: int, c: list) -> int:
    c.sort(reverse=True)
    length_c = len(c)
    total = 0
    for i in range(length_c):
        total += (int(i/k)+1)*c[i]
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
