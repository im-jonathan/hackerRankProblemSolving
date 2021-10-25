# Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
# It must be greater than the original word
# It must be the smallest word that meets the first condition
# Example
# w = abcd
# The next largest word is abdc.
# Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

# Function Description
# Complete the biggerIsGreater function in the editor below.
# biggerIsGreater has the following parameter(s):
# - string w: a word

# Returns
# - string: the smallest lexicographically higher string possible or no answer

# Input Format
# The first line of input contains T, the number of test cases.
# Each of the next T lines contains w.

# Constraints
# 1 ≤ T ≤ 10^5
# 1 ≤ length of w ≤ 100
# w will contain only letters in the range ascii[a..z].

# Sample Input 0
#     5
#     ab
#     bb
#     hefg
#     dhck
#     dkhc

# Sample Output 0
#     ba
#     no answer
#     hegf
#     dhkc
#     hcdk

# Sample Input 1
#     6
#     lmno
#     dcba
#     dcbb
#     abdc
#     abcd
#     fedcbabcd

# Sample Output 1
#     lmon
#     no answer
#     no answer
#     acbd
#     abdc
#     fedcbabdc

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def biggerIsGreater(w):
    # Write your code here
    w = list(w[::-1])
    done = 0
    for i in range(1, len(w)):
        if w[i-1] > w[i]:
            for j in range(i):
                if w[j] > w[i]:
                    w[j], w[i] = w[i], w[j]
                    w = sorted(w[:i])[::-1] + w[i:]
                    return "".join(w[::-1])

    else:
       return "no answer"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
