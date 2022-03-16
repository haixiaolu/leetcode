"""
建图
- 如果一开始就构建图， 每一个单词都需要和除他以外的另外的单词进行比较， 复杂度是O(n * wordLen)
- 为此， 我们在遍历一开始， 把所有的单词列表放进一个哈希表中， 然后在遍历的时候构建图， 每一次得到在单词列表里可以转换的单词， 
  复杂度是O（26 * wordLen)
- 使用BFS
"""
import collections


def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if len(word_set) == 0 or endWord not in word_set:
        return 0

    if beginWord in word_set:
        word_set.remove(beginWord)

    queue = collections.deque()
    queue.append(beginWord)

    visited = set()
    visited.add(beginWord)

    word_len = len(beginWord)
    step = 1
    while queue:
        current_size = len(queue)
        for i in range(current_size):
            word = queue.popleft()

            word_list = list(word)
            for j in range(word_len):
                origin_char = word_list[j]

                for k in range(26):
                    word_list[j] = chr(ord("a") + k)
                    next_word = "".join(word_list)
                    if next_word in word_set:
                        if next_word == endWord:
                            return step + 1

                        if next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)
                word_list[j] = origin_char
        step += 1
    return 0
