"""
1. 贪心 （跳格子）
    1. 当遍历到index遇到1的时候， 说明这个位置有花， 那必然从index + 2的位置才能种花。 因此碰到1时， 直接跳过下一格
    2. 当遍历到index遇到0时， 由于每次碰到1都是跳2格， 因此前一格必定是0， 此时只需要判断下一格是不是1即可得出index这一格能不能种花， 
        - 如果能种， 令n减一， 然后这个位置就按照遇到1时处理， 即跳2格
        - 如果index的后一格是1， 说明这个位置不能种花且之后也不可能种花， 直接跳过3格
    3. 当n减为0时， 说明可以种入n朵花， 则可以直接退出遍历返回true。 如果遍历结束n没有减到0，说明最多种入的花的数量小于n， 则返回False
"""


def canPlaceFlowers(flowerbed, n):
    i, length = 0, len(flowerbed)

    while i < length and n > 0:
        if flowerbed[i] == 1:
            i += 2
        # i == length - 1说明已经遍历到最后一个元素了，
        # 因此， i + 1可以看作是没种花
        elif i == length - 1 or flowerbed[i + 1] == 0:
            n -= 1
            i += 2
        else:
            i += 3
    return n <= 0
