# Jack and Daniel are friends. Both of them like letters, especially uppercase ones.
# They are cutting uppercase letters from newspapers, and each one of them has his collection of letters stored in a stack.
# One beautiful day, Morgan visited Jack and Daniel. He saw their collections. He wondered what is the lexicographically minimal string made of those two collections. He can take a letter from a collection only when it is on the top of the stack. Morgan wants to use all of the letters in their collections.
# As an example, assume Jack has collected a=[A,C,A] and Daniel has b=[B,C,F]. The example shows the top at index 0 for each stack of letters. Assemble the string as follows:
#     Jack	Daniel	result
#     ACA	    BCF
#     CA	    BCF	    A
#     CA	    CF	    AB
#     A	    CF	    ABC
#     A	    CF	    ABCA
#             F	    ABCAC
#                     ABCACF
# Note the choice when there was a tie at CA and CF.

# Function Description
# Complete the morganAndString function in the editor below.
# morganAndString has the following parameter(s):
# - string a: Jack's letters, top at index
# - string b: Daniel's letters, top at index

# Returns
# - string: the completed string

# Input Format

# The first line contains the an integer t, the number of test cases.
# The next t pairs of lines are as follows:
# - The first line contains string a
# - The second line contains string b.

# Constraints
# 1 ≤ T ≤ 5
# 1 ≤ |a|, |b| ≤ 10^5
# a and b contain upper-case letters only, ascii[A-Z].

# Sample Input
#     2
#     JACK
#     DANIEL
#     ABACABA
#     ABACABA

# Sample Output
#     DAJACKNIEL
#     AABABACABACABA

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def morganAndString(a: str, b: str) -> str:
    # Write your code here
    answer = ''
    a += '~'
    b += '~'
    i = 0
    j = 0
    while a[i] != '~' or b[j] != '~':
        if a[i] != '~' and a[i:] < b[j:]:
            answer += a[i]
            i += 1
        else:
            answer += b[j]
            j += 1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
