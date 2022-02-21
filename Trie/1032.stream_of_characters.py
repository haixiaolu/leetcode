"""
- 将单词反向插入字典树中
- 从后往前查找每一个字母在不在根节点
- 如果在， 是否存在叶子节点， 存在返回True， 不存在则返回当前节点， 并且以该节点为根， 继续查下下个字母
- 如果不在，直接返回False
"""


class StreamChecker:
    def __init__(self, words):
        self.root = {}
        self.char = ""
        for word in words:  # 将单词反向插入
            self.insert(word[::-1])

    def insert(self, word):  # 插入下一个单词
        r = self.root
        for s in word:
            if s not in r:
                r[s] = {}
            r = r[s]
        r["#"] = 1

    def search(self, word, r):  # 查询某一个字母是否在当前节点的子节点中
        for s in word:
            if s not in r:
                return False, None
            r = r[s]
        if "#" not in r:  # 没有根节点，记录当前r， 避免下次从头开始
            return False, r
        return True, None  # 返回一个合法结构

    def query(self, letter):
        self.char += letter  # 将每次的字母加入
        r = self.root
        for w in self.char[::-1]:  # 反向查找
            flag, r = self.search(w, r)
            if flag:  # 如果存在, 返回True
                return True
            elif r is None:  # 如果当前字母不在子节点中， 后续也不可能存在合法的后缀， 使得该后缀在数组中
                return False
        return False
