"""
1. index
2. character mapping with dictionary
"""


# def isIsomorphic(s, t):
#     for i in range(len(s)):
#         if s.index(s[i]) != t.index(t[i]):
#             return False
#     return True

# method 2:
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            # case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1

            # case 2: either mapping doesn't exist in one of the dictionaries or mapping
            # doesn't match in either of the dictionaries or both dictionaries
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
        return True