# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:
# There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

# Example
# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5]
# word = 'torn'

# The heights are t=2, o=1, r=1 and n=1. The tallest letter is 2 high and there are 4 letters. The hightlighted area will be 2*4=8mm^2 so the answer is 8.

# Function Description
# Complete the designerPdfViewer function in the editor below.
# designerPdfViewer has the following parameter(s):
# - int h[26]: the heights of each letter
# - string word: a string

# Returns
# int: the size of the highlighted area

# Input Format
# The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
# The second line contains a single word consisting of lowercase English alphabetic letters.

# Constraints
# 1 ≤ h[?] ≤ 7, where ? is an English lowercase letter.
# word contains no more than 10 letters.

# Sample Input 0
#     1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
#     abc

# Sample Output 0
#     9

# Sample Input 1
#     1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
#     zaba

# Sample Output 1
#    28


#!/bin/python3
import math
import os
import random
import re
import sys
from string import ascii_lowercase
#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#


def designerPdfViewer(h: list, word: str) -> int:
    # Write your code here
    letters = ascii_lowercase
    len_word = len(word)
    hight_letter = 0
    for i in word:
        hight_letter = max(hight_letter, h[letters.index(i)])
    word_area = len_word * hight_letter
    return word_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
