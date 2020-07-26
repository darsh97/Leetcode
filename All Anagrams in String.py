from typing      import *
from itertools   import *
from collections import *
from math        import *
from bisect      import *

'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        cnt = Counter(p)
        total = sum(map(ord, p))
        window_t = sum(map(ord, s[:len(p)]))
        window_c = Counter(s[:len(p)])
        l = []
        if cnt == window_c and total == window_t:
            l.append(0)
        for i in range(n, len(s)):
            window_t -= ord(s[i - n]);
            window_t += ord(s[i])
            window_c[s[i - n]] -= 1
            window_c[s[i]] += 1

            if not window_c[s[i - n]]:
                del window_c[s[i - n]]

            if total == window_t:
                if cnt == window_c:
                    l.append(i - (n - 1))
        return l