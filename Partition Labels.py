from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given. We want to partition 
this string into as many parts as possible so that each letter appears in at most one part,
 and return a list of integers representing the size of these parts.
'''


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        idx = defaultdict(list)
        l = []
        for i, e in enumerate(S):
            if e not in idx or len(idx[e]) == 1:
                idx[e].append(i)
            else:
                idx[e][-1] = i

        values = [*idx.values()]
        res = [values[0]]

        for i in range(1, len(values)):
            v = values[i]
            if res[-1][0] <= v[0] <= res[-1][-1]:
                if v[-1] > res[-1][-1]:
                    res[-1][-1] = v[-1]
            else:
                res.append(v)

        for i in range(len(res)):
            res[i] = (res[i][-1] - res[i][0]) + 1

        return res