from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Input:nums = [1,1,1], k = 2
Output: 2
'''

class Solution:
    def subarraySum(self, nums: list, k: int) -> list:
        d = defaultdict(int)
        cnt = 0
        t = 0
        for i, e in enumerate(nums):
            t += e
            d[t] += 1
            if t == k: cnt += 1
            if t - k in d:
                cnt += d[t - k] if k else d[t-k]-1
        return cnt