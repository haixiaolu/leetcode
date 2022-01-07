class Solution:
    def trappingRainWater(self, heights):

        stack = []
        ans = 0
        n = len(heights)

        for i, h in enumerate(heights):
            while stack and h > heights[stack[-1]]:
                peek = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(heights[left], heights[i]) - heights[peek]
                ans += currWidth + currHeight

            stack.append(i)

        return ans


s = Solution()
print(s.trappingRainWater([0, 1, 2, 3, 4, 6, 3, 2]))
print(s.trappingRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
