# DNA is a nucleic acid present in the bodies of living things. Each piece of DNA contains a number of genes, some of which are beneficial and increase the DNA's total health. Each gene has a health value, and the total health of a DNA is the sum of the health values of all the beneficial genes that occur as a substring in the DNA. We represent genes and DNA as non-empty strings of lowercase English alphabetic letters, and the same gene may appear multiple times as a susbtring of a DNA.
# Given the following:
# - An array of beneficial gene strings, genes = [g0,g1,...,gn-1]. Note that these gene sequences are not guaranteed to be distinct.
# - An array of gene health values, health = [h0,h1,...,hn-1], where each hi is the health value for gene gi.
# - A set of s DNA strands where the definition of each strand has three components, start, end, and d, where string d is a DNA for which genes gstart,...,gend are healthy.
# Find and print the respective total healths of the unhealthiest(minimum total health) and healthiest(maximum total health) strands of DNA as two space-separated values on a single line.

# Input Format
# The first line contains an integer, n, denoting the total number of genes.
# The second line contains n space-separated strings describing the respective values of g0,g1,...,gn-1(i.e., the elements of genes).
# The third line contains n space-separated integers describing the respective values of h0,h1,...,hn-1(i.e., the elements of health).
# The fourth line contains an integer, s, denoting the number of strands of DNA to process.
# Each of the s subsequent lines describes a DNA strand in the form start end d, denoting that the healthy genes for DNA strand d are gstart,...,gend and their respective correlated health values are hstart,...,hend.

# Constraints
# 1 ≤ n, s ≤ 10^5
# 0 ≤ hi ≤ 10^7
# 0 ≤ first ≤ last ≤ n
# 1 ≤ the sum of the lengths of all genes and DNA strands ≤ 2x10^6
# It is guaranteed that each gi consists of lowercase English alphabetic letters only(i.e., a to z).

# Output Format
# Print two space-separated integers describing the respective total health of the unhealthiest and the healthiest strands of DNA.

# Sample Input 0
#     6
#     a b c aa d b
#     1 2 3 4 5 6
#     3
#     1 5 caaab
#     0 4 xyz
#     2 4 bcdybc

# Sample Output 0
#     0 19

#!/bin/python3

import math
import os
import random
import re
import sys
from math import inf
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict


def getHealth(seq, first, last, largest):
    h, ls = 0, len(seq)

    for f in range(ls):
        for j in range(1, largest+1):
            if f+j > ls:
                break
            sub = seq[f:f+j]
            if sub not in subs:
                break
            if sub not in gMap:
                continue
            ids, hs = gMap[sub]
            h += hs[bRight(ids, last)]-hs[bLeft(ids, first)]
    return h


if __name__ == '__main__':

    n = int(input())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))

    gMap = defaultdict(lambda: [[], [0]])
    subs = set()
    for i, gene in enumerate(genes):
        gMap[gene][0].append(i)
        for j in range(1, min(len(gene), 500)+1):
            subs.add(gene[:j])

    for v in gMap.values():
        for i, ix in enumerate(v[0]):
            v[1].append(v[1][i]+health[ix])

    largest = max(list(map(len, genes)))
    hMin, hMax = inf, 0

    s = int(input())
    for s_itr in range(s):
        firstLastd = input().split()
        first = int(firstLastd[0])
        last = int(firstLastd[1])
        d = firstLastd[2]
        h = getHealth(d, first, last, largest)
        hMin, hMax = min(hMin, h), max(hMax, h)

    print(hMin, hMax)
