"""
1. 横向扫描
   用LCP(S1,...Sn)表示字符串S1,...Sn的最长公共前缀， 可以得到以下结论： `LCP(S1,...Sn) = LCP(LCP(S1, S2), LCP(S3, S4))`
   基于该结论， 可以得到一种查找字符串数组中的最长公共前缀的简单方法： 
   - 依次遍历字符串数组中的每个字符串， 更新公告前缀， 
   - 当遍历完所有的字符串以后，即可得到字符串数组中的最长公共前缀。
   - 如果在尚未遍历完所有的字符串时， 最长公共前缀已经是空串， 则最长公共前缀一定是空串，因此不需要继续遍历剩下的字符串，直接返回空串即可。
"""


# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""

#         prefix = strs[0]
#         count = len(strs)
#         for i in range(1, count):
#             prefix = self.lcp(prefix, strs[i])
#             if not prefix:
#                 break
#         return prefix

#     def lcp(self, s1, s2):
#         if not s1 or not s2:
#             return ""

#         length, index = min(len(s1), len(s2)), 0
#         while index < length and s1[index] == s2[index]:
#             index += 1
#         return s1[:index]


# Method 2, 内置zip()函数
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        res = ""
        for tmp in zip(*strs):
            # print(tmp)
            tmp_set = set(tmp)
            # print(tmp_set)
            if len(tmp_set) == 1:
                res += tmp[0]
                # print(res)
            else:
                break
        return res


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
