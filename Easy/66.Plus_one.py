"""
Question: given a large integer represented as an integer array disits, where each digits[i] is the ith digit of the integer. 
          The digits are ordered from most significant to least significant in left-to-right order. The large integer does not 
          contain any leading 0's 

          Increment the large integer by one and return the resulting array of digits

          Input: digits = [1, 2, 3], Output: [1, 2, 4]
"""

"""
Approach: 找出最长的后缀9
         当我们对数组digits加一时， 我们只需要关注digits的末尾出现了多少个9即可， 考虑三种情况
         - 如果digits的末尾没有9， 我们直接将末尾的数加一， 得到【1， 2， 4】 并返回
         - 如果digits的末尾有若干个9， 例如【1， 2， 3， 9， 9】， 那么我们只需要找出从末尾开始的第一个不为9的元素，
           即3， 将该元素加一，得到【1， 2， 4， 9， 9】， 随后将末尾的9全部置零， 得到【1， 2， 4， 0， 0】
        - 如果digits的所有元素都是9， 例如【9， 9， 9， 9，9】， 那么答案为【1， 0， 0， 0， 0，0】， 我们只需要构造一个长度比digits多一的新数组，
          将首元素置为1， 其余元素置为0即可
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits中所有的元素均为9
        return [1] + [0] * n


# Time: O(n)
# Space: O(1)