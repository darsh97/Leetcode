from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Input: s = "bab", t = "aba"
Output: 1
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return len(s) - sum((Counter(s) & Counter(t)).values())

