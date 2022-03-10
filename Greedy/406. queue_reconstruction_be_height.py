"""
1. 排序 + 贪心
    我们首先对数对进行排序， 按照数对的元素1降序排序， 元素2升序排序
    - 因为元素1进行降序排序， 对于每个元素， 在其之前的元素的个数， 就是大于等于他的元素的数量
    - 按照元素2正向排序， 我们希望k大的尽量在后面，减少插入的次数
"""


def reconstrucQueue(people):
    # for loop with extra space
    res = []
    people.sort(key=lambda x: (-x[0], x[0]))
    for p in people:
        if len(res) <= p[1]:
            res.append(p)
        elif len(res) > p[1]:
            res.insert(p[1], p)
    return res


# while with no extra space


def reconstrucQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    i = 0
    while i < len(people):
        if i > people[i][1]:
            people.insert(people[i][1], people[i])
            people.pop(i + 1)
        i += 1
    return people
