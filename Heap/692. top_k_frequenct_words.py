"""
Follow up : heap
"""
import collections
import heapq


class Word:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        if self.cnt > other.cnt:
            return False
        elif self.cnt < other.cnt:
            return True
        else:
            return self.word > other.word


class Solution:
    def topFrequent(self, words, k):
        q = []
        freq = collections.Counter(words)
        for word, cnt in freq.items():
            heapq.heappush(q, Word(word, cnt))
            if len(q) > k:
                heapq.heappop(q)
        res = []
        while q:
            res.append(heapq.heappop(q).word)
        return res[::-1]