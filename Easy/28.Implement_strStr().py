"""
Question: Implement strStr()

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack

    Clarification:
    what should we return when needle is an empty string? This is a great question to ask during the interview
"""
"""
解法： KMP（Knuth-Morris-Pratt)， 暴力
"""


class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
