from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/monotone-increasing-digits/

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Input: N = 332
Output: 299

'''

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        sn = [*str(N)]
        for i in range(len(sn) - 1):
            if sn[i] > sn[i + 1]:
                p = sn.index(sn[i])
                return int(''.join(sn[:p]) + str(int(sn[p])-1) + '9'*(len(sn[p:]) - 1))
        return N

