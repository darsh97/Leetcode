from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/max-chunks-to-make-sorted/

Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], 
we split the array into some number of "chunks" (partitions), and individually sort each chunk.  
After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Input: arr = [4,3,2,1,0]
Output: 1

Input: arr = [1,0,2,3,4]
Output: 4
'''

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        tt = t = cnt = 0
        for i in range(len(arr)):
            t  += arr[i]
            tt += i
            cnt  += t == tt
        return cnt