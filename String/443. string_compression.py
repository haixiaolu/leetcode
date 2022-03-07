"""
1. 双指针 + 滑动窗口
  - 初始化point指针用于返回下标， left， right指针用于遍历数组过程中扩张， 缩减滑动窗口
  - 加一个小操作： 对于python的动态列表， 我们可以给charts追加一个空字符作为哨兵， 避免循环到结果时需要最后判断一次窗口内的数据
  - 然后开始移动right指针， 当发现right指针指向的内容不等于left时， 我们将point指针更新为left指针的内容， 并右移point
  - 然后计算right与left的距离，当距离大于1时， 将长度转化为字符串， 按位对point下标赋值
  - 完成后将left = right
  - 重复3， 4， 5, 最终返回point指针的位置即可
"""


class Solution:
    def compress(self, chars):
        point = left = 0
        chars.append("")
        for right, char in enumerate(chars):
            if char != chars[left]:
                chars[point] = chars[left]
                point += 1
                distance = right - left
                if distance > 1:
                    # 将长度转化为字符串， 按位对point下标赋值
                    for digit in str(distance):
                        chars[point] = digit
                        point += 1
                left = right
        return point