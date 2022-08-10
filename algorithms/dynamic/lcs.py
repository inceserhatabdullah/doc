#!/usr/bin/env python3

# The longest common subsequence in Python
"""                 LONGEST COMMON SUBSEQUENCE
# * The longest common subsequence (LCS) is defined as the longest subsequence that is common to all the given sequences,
provided that the elements of the subsequence are not required to occupy consecutive positions within the original sequences.
# ? in compressing genome resequencing data
# ? to authenticate users within their mobile phone through in-air signatures
# * https://www.programiz.com/dsa/longest-common-subsequence
"""

# Function to find lcs_algo
def lcs_algo(_, __, _len, __len):
    L = [[0 for x in range(__len+1)] for x in range(_len+1)]

    # Building the matrix in bottom-up way
    for i in range(_len+1):
        for j in range(__len+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif _[i-1] == __[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[_len][__len]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = _len
    j = __len
    
    while i > 0 and j > 0:

        if _[i-1] == __[j-1]:
            lcs_algo[index-1] = _[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences
    print("_ : " + _ + "\n__ : " + __)
    print("LCS: " + "".join(lcs_algo))


_ = "AABBBCD"
__ = "CBDA"

lcs_algo(_, __, len(_), len(__))