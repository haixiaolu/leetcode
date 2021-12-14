"""
Question: given an integer array nums and an integer val, remove all occurrences of val in nums in-place
          The relative order of the elements may be changed. 
"""

"""
Answer: 双指针优化
思路： 如果要移除的元素恰好在数组的开头， 例如序列【1， 2， 3， 4， 5】， 当val为1时， 我们需要把每一个元素都左移一位。 
      注意到题目中说：【元素的顺序可以改变】实际上我们可以直接将最后一个元素5移动到序列开头。 取代元素1， 得到序列【5， 2， 3， 4】，
      同样满足题目的要求。 这个优化在序列中val元素的变量较少时非常有用

算法： 如果左指针start指向的元素等于val， 此时将右指针right指向的元素复制到左指针start的位置， 然后右指针end左移一位。 
      如果赋值过来的元素恰好也等于val， 可以继续把右指针end指向的元素的值赋值过来 （左指针left指向的等于val的元素的位置继续被覆盖） 
      直到左指针指向的元素的位置不等于val为止

"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = nums[start]
                end = end - 1
            else:
                start += 1
        return start


# Time: O(n)
# Space: O(1)