from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Input: "cdadabcc"
Output: "adbc"

Input: "ecbacba"
Output: "eacb"

'''
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if not s: return ""
        lastidx = {e:i for i, e in enumerate(s)}
        stack   = [s[0]]
        seen    = {s[0]}

        for i in range(1, len(s)):
            if s[i] not in seen:
                while stack and s[i] not in seen and s[i] < stack[-1] and lastidx[stack[-1]] >= i:
                    seen.remove(stack.pop())
                stack.append(s[i])
            seen.add(s[i])

        return ''.join(stack)