from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/shifting-letters/

We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.
'''


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        T = 0
        A = [0]

        for e in shifts:
            E = e % 26
            T += E
            A.append(T)

        L = []

        for i in range(len(shifts)):
            o = ord(S[i]) - 96
            X = (o + (T - A[i]))
            L.append(chr((X % 26) + 96) if X % 26 else 'z')

        return ''.join(L)

