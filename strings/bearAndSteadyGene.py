# A gene is represented as a string of length n (where is divisible by 4), composed of the letters A, C, T, and G. It is considered to be steady if each of the four letters occurs exactly n/4 times. For example, GACT and AAGTGCCT are both steady genes.
# Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string gene. It is not necessarily steady. Fortunately, Limak can choose one(maybe empty) substring of gene and replace it with any string of the same length.
# Modifying a large substring of bear genes can be dangerous. Given a string gene, can you help Limak find the length of the smallest possible substring that he can replace to make gene a steady gene?
# Note: A substring of a string is a subsequence made up of zero or more contiguous characters of s.
# As an example, consider gene=ACTGAAAG. The substring AA just before or after G can be replaced with CT or TC. One selection would create ACTGACTG.

# Function Description
# Complete the steadyGene function in the editor below. It should return an integer that represents the length of the smallest substring to replace.
# steadyGene has the following parameter:
# - gene: a string

# Input Format
# The first line contains an interger n divisible by 4, that denotes the length of a string gene.
# The second line contains a string gene of length n.

# Constraints
# 4 ≤ n ≤ 500000
# n is divisible by 4
# gene[i] ∈ [CGAT]

# Subtask
# 4 ≤ n ≤ 2000 in tests worth 30% points.

# Output Format
# Print the length of the minimum length substring that can be replaced to make gene stable.

# Sample Input
#     8
#     GAAATAAA

# Sample Output
#     5

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def balanced(l, d):
    ans = True
    for k, v in d.items():
        if v > l:
            ans = False
            break
    return ans
#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#


def steadyGene(gene: str) -> int:
    # Write your code here
    l = len(gene)//4
    gene_count = Counter(gene)
    start = 0
    end = 0
    count = 10**6
    while start < n and end < n:
        if not balanced(l, gene_count):
            gene_count[gene[end]] -= 1
            end += 1

        else:
            count = min(count, end-start)
            gene_count[gene[start]] += 1
            start += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
