from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
'''

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A: return 0
        A.sort()
        seen = {A[0]}
        cnt  = 0

        for i in range(1, len(A)):
            if A[i] in seen:
                cnt += (A[i-1] - A[i]) + 1
                A[i] = A[i-1]+ 1

            mx = A[i - 1]
            seen.add(A[i])

        return cnt