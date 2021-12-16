# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
#     Original alphabet:      abcdefghijklmnopqrstuvwxyz
#     Alphabet rotated + 3:    defghijklmnopqrstuvwxyzabc
# Example
# s = There´s-a-starman-waiting-in-the-sky
# k = 3
# The alphabet is rotated by 3, matching the mapping above. The encrypted string is Wkhuh'v-d-vwduwpdq-zdlwlqj-lq-wkh-vnb.
# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Function Description
# Complete the caesarCipher function in the editor below.
# caesarCipher has the following parameter(s):
# - string s: cleartext
# - nt k: the alphabet rotation factor

# Returns
# string: the encrypted string

# Input Format
# The first line contains the integer, n, the length of the unencrypted string.
# The second line contains the unencrypted string, s.
# The third line contains k, the number of letters to rotate the alphabet by.

# Constraints
# 1 ≤ n ≤ 100
# 0 ≤ k ≤ 100
# s is a valid ASCII string without any spaces.

# Sample Input
#     11
#     middle-Outz
#     2

# Sample Output
#     okffng-Qwvb

# Explanation
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated + 2:    cdefghijklmnopqrstuvwxyzab
# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# - -
# O -> Q
# u -> w
# t -> v
# z -> b

#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s: str, k: int) -> str:
    # Write your code here
    data = ""
    for letter in s:
        if letter.isupper():
            i = (uppers.index(letter)+k) % 26
            data += uppers[i]
        elif letter.islower():
            i = (lowers.index(letter)+k) % 26
            data += lowers[i]
        else:
            data += letter
    return data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lowers = tuple(string.ascii_lowercase)
    uppers = tuple(string.ascii_uppercase)
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
