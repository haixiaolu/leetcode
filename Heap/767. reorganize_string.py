"""
题解一： 最大堆贪心
- 首先统计每个字母的出现次数， 出现次数大于0的加入最大堆
- 将最大堆的元素个数大于1时， 每次从最大堆取出2个字母， 拼接到重构的字符串， 然后将2个字母的出现次数分别减一，并将剩余出现次数大于
  0的字母重新加入最大堆
- 如果最大堆变成空， 则已经完成字符串的重构， 如果最大堆剩下一个元素， 则取出最后一个字母， 拼接到重构的字符串
- 对于长度为n的字符串， 共有n/2次每次从最大堆取出2个字母的操作， n是奇数的时候， 还有一次从最大堆取出一个字母的操作
"""
import collections
import heapq


def reorganizeString(s):
    if len(s) < 2:
        return s

    length = len(s)
    counts = collections.Counter(s)
    maxCount = max(counts.items(), key=lambda x: x[1])[1]
    if maxCount > (length + 1) // 2:
        return ""

    queue = [(-x[1], x[0]) for x in counts.items()]
    heapq.heapify(queue)
    ans = []

    while len(queue) > 1:
        _, letter1 = heapq.heappop(queue)
        _, letter2 = heapq.heappop(queue)
        ans.extend([letter1, letter2])
        counts[letter1] -= 1
        counts[letter2] -= 1
        if counts[letter1] > 0:
            heapq.heappush(queue, (-counts[letter1], letter1))
        if counts[letter2] > 0:
            heapq.heappush(queue, (-counts[letter2], letter2))
    if queue:
        ans.append(queue[0][1])

    return "".join(ans)
