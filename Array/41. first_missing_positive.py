class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # 检查1是否存在与数组中， 如果没有， 则已经完成， 1即为答案
        if 1 not in nums:
            return 1

        # 将负数， 0， 和大于n的数替换为1， 此时， 数组中所有的元素均为正数
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 遍历数组， 当读到数字a的时候，给第a - 1位的元素加上负号， 重要重复元素， 只能改变一次符号
        for i in range(n):
            a = abs(nums[i]) - 1  # abs防止当前数是负数
            nums[a] = -abs(nums[a])  # 把正数变成负数

        # 再次遍历数组， 返回第一个元素的下标 + 1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


obj = Solution()
print(obj.firstMissingPositive([1, 2, 4, -1, 0]))
print(obj.firstMissingPositive([1, 2, 0]))