from typing import *

'''
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        st: List[str] = [*s]
        stack: List[int] = []
        close: List[int] = []
        pair: Mapping[int, int] = {}

        for i, b in enumerate(s):
            if b == '(': stack.append(i)
            if b == ')':
                pair[i] = stack.pop()
                close.append(i)

        for c in close:
            start = pair[c]
            end = c
            st[start: end + 1] = st[start: end + 1][::-1]

        return ''.join(e for e in st if e.isalpha())
