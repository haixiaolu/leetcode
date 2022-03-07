"""
1. 模拟
 对于每一行， 我们首先确定最多可以放置多少单词，这样可以得到改行的空格个数， 从而确定该行单词之间的空格个数
 根据题目中填充空格的细节， 我们分以下三种情况讨论：
 - 当前行是最后一行： 单词左对齐， 且单词之间应只用一个空格， 在行末填充剩余空格
 - 当前行不是最后一行： 单词左对齐， 且单词之间应只用一个空格， 在行末填充空格
 - 当前行不是最后一行， 且不只一个单词， 设当前行单词数为numWords， 空格数为numSpaces, 我们需要将空格均分配
   在单词之间，则单词之间至少有 avgSpace = (numsSpace / numWords - 1) 个空格，对于多出来的 `extraSpace = numSpaces mod(numWords - 1)`
    个空格，应填在extraSpace个单词之前，因此， 前extraSpace个单词之间的空格数为 `avgSpace + 1`个空格
"""


def blank(n):
    return " " * n


class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        right, n = 0, len(words)
        while True:
            left = right  # 当前行的第一个单词在words的位置
            sumLen = 0  # 统计这一行单词的长度
            # 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
            while right < n and sumLen + len(words[right]) + right - left <= maxWidth:
                sumLen += len(words[right])
                right += 1

            # 当前行是最后一行： 单词左对齐， 且单词之间应只用一个空格， 在行末填充剩余空格
            if right == n:
                s = "".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break
            numWords = right - left
            numSpaces = maxWidth - sumLen

            # 当前行只有一个单词，该单词左对齐，在行末填充空格
            if numWords == 1:
                ans.append(words[left] + blank(numSpaces))
                continue

            # 当前行不只一个单词
            avgSpace = numSpaces // (numWords - 1)
            extraSpace = numSpaces % (numWords - 1)
            s1 = blank(avgSpace + 1).join(
                words[left : left + extraSpace + 1]
            )  # 拼接额外加一个空格的单词
            s2 = blank(avgSpace).join(words[left + extraSpace + 1 : right])  # 拼接其余的单词
            ans.append(s1 + blank(avgSpace) + s2)
        return ans