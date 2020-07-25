from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([(-1, float("-inf"))])
        mxlst = []
        for i in range(k):
            if nums[i] < dq[-1][-1]:
                dq.append((i, nums[i]))
            else:
                while dq and dq[-1][-1] < nums[i]:
                    dq.pop()
                dq.append((i, nums[i]))

        mxlst.append(dq[0][-1])


        for i in range(k, len(nums)):
            if i - k == dq[0][0]:
                dq.popleft()
            if dq and nums[i] < dq[-1][-1]:
                dq.append((i, nums[i]))
            else:
                while dq and dq[-1][-1] < nums[i]:
                    dq.pop()
                dq.append((i, nums[i]))
            mxlst.append(dq[0][-1])

        return mxlst
