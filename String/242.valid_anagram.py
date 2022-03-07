"""
1. One line of sorted or Counter
"""


class Solution:
    def isAnagram(s, t):
        return sorted(s) == sorted(t)

    # def isAnagram(self, s, t):
    #     return collections.Counter(s) == collections.Counter(t)


"""
2. 哈希表
    从另一个角度， t是s的异位词等价于【两个字符串中字符出现的种类和次数均相等】， 由于字符串只包含26个小写字母， 因为我们可以维护一个长度为
    26的频次数组table， 
    - 先遍历记录字符串s中字符出现的频次， 然后遍历字符串t， 减去table中对应的频次。 
    - 如果出现table[i] < 0， 说明t中的字符串中存在比s中的字符串多出来的字符， 则不是异位词
"""


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        table = [0] * 26
        for i in s:
            table[ord(i) - ord("a")] += 1

        for j in t:
            table[ord(j) - ord("a")] -= 1

        for item in table:
            if item != 0:
                return False
        return True