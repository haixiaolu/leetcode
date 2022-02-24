"""
使用哈希表存储每一组字母异位词，哈希表的键位一组字母异位词标志
哈希表的键位一组字母异位词列表
"""
# 排序
import collections


def groupAnagrams(strs):
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)

    return list(mp.values())


# 计数
"""
由于互为字母异位词的连个字符串包含的字母相同， 因此两个字符串的相同字母出现的次数一定是相同的
故可以将每个字母出现的次数使用字符串表示， 做为哈希表的键
"""


def groupAnagrams(strs):
    mp = collections.defaultdict(list)
    for st in strs:
        counts = [0] * 26
        for ch in st:
            counts[ord(ch) - ord("a")] += 1
        # 需要将list转化为tuple才能进行哈希
        mp[tuple(counts)].append(st)
    return list(mp.values())
