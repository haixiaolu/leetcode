"""
write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string ""
Example: 
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Answer: 
1. 横向扫描：
    用LCP(S1...Sn)表示字符串S1...Sn的最长公共前缀。 可以得到以下结论：
    LCP(S1...Sn)=LCP(LCP(LCP(S1, S2), S3),...Sn)
    依次遍历字符串数组中的每个字符串， 对于每个遍历到的字符串，更新最长公共前缀， 当遍历完所有的字符串以后，
    即可得到字符串数组中的最长公共前缀。 

    如果在尚未遍历完所有的字符串时， 最长公共前缀已经时空串， 则最长公共前缀一定是空串，因此不需要继续
    遍历剩下的字符串，直接返回空串即可
"""
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix, count = strs[0], len(strs)
    for i in range(1, count):
        prefix = lcp(prefix, strs[i])
        if not prefix:
            break

    return prefix


def lcp(str1, str2):
    length, index = min(len(str1), len(str2)), 0
    while index < length and str1[index] == str2[index]:
        index += 1
    return str1[:index]


# Time: O(mn), m是字符串数组中的字符串平均长度，n是字符串的数量， 最坏情况下， 字符串数组中的
#                每个字符串的每个字符都会被比较一次

# Space: O(1), 使用额外空间复杂度为常数

"""
2. 纵向扫描：
    从前往后遍历所有字符串的每一列， 比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，如果
    不相同则当前不再属于公共前缀， 当前列之前的部分为最长公共前缀
"""


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    length, count = len(strs[0]), len(strs)
    for i in range(length):
        c = strs[0][i]
        if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
            return strs[0][:i]
    return strs[0]


# Time: O(mn)
# Space: O(1)

"""
3. 分治

注意到LCP的巨酸满足结合律， 有以下结论：
    LCP(S1...Sn) = LCP(LCP(S1...Sk), LCP(SK+1...Sn))
    其中LCP(S1...Sn)是字符串S1...Sn的最长公共前缀， 1 < K < n

可以使用分治法得到字符串数组中的最长公共前缀， 对于问题LCP(Si...Sj),可以分解成两个子问题LCP(Si...Smid)与LCP(Smid + 1,...Sj),
其中mid = i + j / 2， 对两个子问题分别求解， 然后对两个子问题的解计算最长公共前缀， 即为原问题的解
"""


def longestCommonPrefix(strs: List[str]) -> str:
    def lcp(start, end):
        if start == end:
            return strs[start]

        mid = (start + end) // 2
        lcp_left, lcp_right = lcp(start, mid), lcp(mid + 1, end)
        min_length = min(len(lcp_left), len(lcp_right))
        for i in range(min_length):
            if lcp_left[i] != lcp_right[i]:
                return lcp_left[:i]

        return lcp_left[:min_length]

    return "" if not strs else lcp(0, len(strs) - 1)


# Time: O(mn)
# Space: O(mlogn), m是字符串数组中的字符串的平均长度， n是字符串的数量， 空间复杂度主要取决于递归调用的层数， 层数最大为logn， 每层需要m的空间存储返回结果

"""
4. 二分查找
   最长公共前缀的长度不会超过字符串数组中的最短字符串的长度， 用minLength表示字符串数组中的最短字符串的长度
   则可以在[0, minLength]的范围内通过二分查找叨叨最长公共前缀的长度，每次取查找范围的中间值mid， 判断每个字符串的长度为mid的前缀是否相同
   如果相同则最长公共前缀的长度一定大于或等于mid， 如果不相同则最长公共前缀的长度一定小于mid， 通过上述方式将查找范围缩小一半， 直到得到最长公共前缀
   的长度
"""


def longestCommonPrefix(strs: List[str]) -> str:
    def isCommonPrefix(length):
        str0, count = strs[0][:length], len(strs)
        return all(strs[i][:length] == str0 for i in range(1, count))

    if not strs:
        return ""

    minLength = min(len(s) for s in strs)
    low, high = 0, minLength
    while low < high:
        mid = (high - low + 1) // 2 + low
        if isCommonPrefix(mid):
            low = mid
        else:
            high = mid - 1
    return strs[0][:low]


# Time: O(mn log m)
# Space : O(1)