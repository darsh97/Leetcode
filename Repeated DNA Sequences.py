from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, 
it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        X = sum((ord(d)*(7**i)for i, d in enumerate(s[:10])))
        D  = {X }
        L = []
        SEEN = set()
        for i in range(10, len(s)):
            PREV = ord(s[i - 10])*7**0
            X = ((X-PREV)//7)+ (ord(s[i])*(7**9))
            if X in D and X not in SEEN:
                L.append(s[i+1-10:i+1])
                SEEN.add(X)
            else:      D[X] = (i+1)-10
        return L

