# James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.
# To do this, he follows two rules:
# 1. He can only reduce the value of a letter by 1, i.e. he can change d to c, but he cannot change c to d or d to b.
# 2. The letter a may not be reduced any further.
# Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.
# Example
# s = cde
# The following two operations are performed: cde → cdd → cdc. Return 2.

# Function Description
# Complete the theLoveLetterMystery function in the editor below.
# theLoveLetterMystery has the following parameter(s):
# - string s: the text of the letter

# Returns
# int: the minimum number of operations

# Input Format
# The first line contains an integer q, the number of queries.
# The next q lines will each contain a string s.

# Constraints
# 1 ≤ q ≤ 10
# 1 ≤ |s| ≤ 10^4
# All strings are composed of lower case English letters, ascii[a-z], with no spaces.

# Sample Input
#     STDIN   Function
#     ----- --------
#     4       q = 4
#     abc     query 1 = 'abc'
#     abcba
#     abcd
#     cba

# Sample Output
#     2
#     0
#     4
#     2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def theLoveLetterMystery(s: str) -> int:
    # Write your code here
    i = 0
    value = 0
    while(i < int(len(s)//2)):
        value += abs(ord(s[i])-ord(s[len(s)-i-1]))
        i += 1
    return value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
