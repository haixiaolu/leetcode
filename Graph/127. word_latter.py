"""
A transformation sequence from word "beginWord" to word "endWord" using a dictionary "wordList" is 
a sequence of words "beginWord -> s1 -> s2 -> ... -> sk, 
Given the two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists
"""
"""
广度优先遍历 + 优化建图
- 每个单词都抽象为一个点，如果两个单词可以只改变一个字母进行转换， 那么说明它们之间有一条双向边
1. 首先为了方便表示，先给每个单词一个编号，即给每个单词分配一个id
2. 创建一个由单词word到id对应的映射wordId， 并将beginWord与wordList中所有的单词都加入这个映射中
3. 之后我们检查endWord是否在该映射中内， 若不存在，则输入无解， 使用【哈希表】实现上面的映射关系
"""
import collections


def ladderLength(beginWord, endWord, wordList):
    def addWord(word):
        if word not in wordId:
            nonlocal nodeNum
            wordId[word] = nodeNum
            nodeNum += 1

    def addEdge(word):
        addWord(word)
        id1 = wordId[word]
        chars = list(word)
        for i in range(len(chars)):
            tmp = chars[i]
            chars[i] = "*"
            newWord = "".join(chars)
            addWord(newWord)
            id2 = wordId[newWord]
            edge[id1].append(id2)
            edge[id2].append(id1)
            chars[i] = tmp

    wordId = dict()
    edge = collections.defaultdict(list)
    nodeNum = 0

    for word in wordList:
        addEdge(word)

    addEdge(beginWord)
    if endWord not in wordId:
        return 0

    dis = [float("inf")] * nodeNum
    beginId, endId = wordId[beginId], wordId[endWord]
    dis[beginId] = 0

    queue = collections.deque([beginId])
    while queue:
        x = queue.popleft()
        if x == endId:
            return dis[endId] // 2 + 1
        for it in edge[x]:
            if dis[it] == float("inf"):
                dis[it] = dis[x] + 1
                queue.append(it)
    return 0
