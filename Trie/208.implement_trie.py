"""
插入字符串：
从字典树的根开始， 插入字符串， 对于当前那字符串对应的子节点， 有两种情况：
- 1. 字符串存在， 沿着指针移动到子节点， 继续处理下一个字符
- 2. 子节点不存在， 创建一个新的子节点， 记录在children数组的对应位置， 然后沿着指针移动到子节点， 继续搜索下一个字符
查找前缀：
从根开始，查找前缀， 对于当前字符对应的子节点， 有两种情况：
- 子节点存在，沿着指针移动到子节点， 继续搜索下一个字符
- 子节点不存在， 说明字典树不包含前缀， 返回空指针
"""


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix):
        return self.searchPrefix is not None
