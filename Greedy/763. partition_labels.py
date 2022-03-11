"""
1. 从左到右遍历字符串， 遍历的同时维护当前片段的开始下标start和结束下标位置end， 初始时start = end = 0
2. 对于每个访问到的字母c， 得到当前字母的最后一次出现的下标位置ENDc， 则当前片段的结束下标一定不会小于ENDc, 因此令end = max(end, ENDc)
3. 当访问到下标end时， 当前片段访问结束， 当前片段的下标范围时[start, end]， 长度为end - start + 1， 将当前片段的长度添加到返回值， 然后令start = end + 1
   继续寻找下一个片段
4. 重复上述过程， 知道遍历完字符串
"""


def partitionLabels(s):
    last = [0] * 26
    for i, ch in enumerate(s):
        last[ord(ch) - ord("a")] + 1

    partition = list()
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ord(ch) - ord("a")])
        if i == end:
            partition.append(end - start + 1)
            start = end + 1
    return partition
