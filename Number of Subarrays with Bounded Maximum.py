from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3

'''

class Solution:

    @staticmethod
    def get_subarray_cnt(n):
        return n * (n + 1) // 2

    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        mx = float("-inf")
        l = lt = gt = g = 0
        t = 0
        for a in A:
            mx = max(a, mx)
            l += a < L
            if L <= a <= R:
                lt += Solution.get_subarray_cnt(l)

                t += lt
                lt = l = 0
            if a > R:
                gt += Solution.get_subarray_cnt(g) - t
                lt = l = g = 0
            g += 1

        return Solution.get_subarray_cnt(g) - t - l if not gt else gt
