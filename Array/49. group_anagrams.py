import collections


def groupAnagrams(strs):

    hashmap = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        hashmap[key].append(st)
        # print(hashmap.keys())
        # print(hashmap.values())

    return list(hashmap.values())


strs = ["ate", "eat", "tea", "bat", "tab", "tan"]
a = groupAnagrams(strs)
print(a)