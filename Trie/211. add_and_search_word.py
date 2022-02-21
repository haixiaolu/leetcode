"""
前缀树的变种
在匹配过程中， 如果遇到了 ".", 则需要对当前节点的所有子树进行遍历， 只要有任何一个子树能最终匹配完成
那么就代表能匹配完成
"""
import collections


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False


class wordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        current = self.root
        for ch in word:
            current = current.children[ch]
        current.isWord = True

    def search(self, word):
        return self.match(word, 0, self.root)

    def match(self, word, index, root):
        if root == None:
            return False
        if index == len(word):
            return root.isWord
        if word[index] != ".":
            return root != None and self.match(
                word, index + 1, root.children.get(word[index])
            )
        else:
            for child in root.children.values():
                if self.match(word, index + 1, child):
                    return True
        return False
