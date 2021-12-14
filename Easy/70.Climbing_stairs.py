"""
Question: You are climbing a staircase. it takes n steps to reach the top. 
          Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Input: n = 2, Output: 2
"""

"""
Approach: 1. Brule Force
          2. Dymnatic programming    
            - start from bottom (bottom up)
            - create a dp array
            - from the right (last one is alway 1, second of last one is also 1, otherwise is outbound)
            - the last third one is adding last two element
            - excepte last 2 elements, always add 2 a time give the previous value 
            - we also don't need to create a array for extra space, we can set two variables for last two elements to 1

            **Same as Fabnacci Sequency**
         
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):

            temp = one
            one = one + two
            two = temp

        return one
