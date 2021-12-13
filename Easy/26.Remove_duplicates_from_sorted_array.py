"""
Question: given an interger array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
          appears only once. The relative order of the elements should be kept the same
"""

"""
Approach: 双指针
    - 当数组nums的长度大于0时， 数组中至少包含一个元素， 在删除重复元素之后也至少剩下一个元素， 因此nums[0]保持原状即可， 从下标1开始删除重复元素
    - 定义两个指针fast和slow分别为快指针和慢指针， 快指针表示遍历数组到达的下标位置，慢指针表示下一个不同元素要填入的下标位置， 初识时两个指针都指向下标1
    - 假设数组nums的长度为n， 将快指针fast依次遍历从1到n-1的每一个位置， 对于每个位置， 如果nums[fast] != nums[fast-1], 说明nums[fast]和之前的元素都不同
      因此将nums[fast]的值复制到nums[slow]， 然后将slow的值加1， 即指向下一个位置
    - 遍历完， 从nums[0]到nums[slow -1]的每个元素都不相同且包含原数组中的每个不同的元素， 因此， 新的长度即为slow， 返回slow即可
"""


class Soultion:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


# Time: O(n)
# Space: O(1)