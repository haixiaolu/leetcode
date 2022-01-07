from typing import List


class Solution:
    def validateStackSequence(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pointer = 0

        for j in pushed:
            stack.append(j)
            while stack and stack[-1] == popped[pointer]:
                stack.pop()
                pointer += 1
        return not stack


s = Solution()
print(s.validateStackSequence(pushed=[1, 2, 3, 4, 5], popped=[5, 4, 3, 2, 1]))
