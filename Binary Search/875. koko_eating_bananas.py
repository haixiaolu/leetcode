import math


class Solution:
    def minEatingSpeed(self, piles, h):
        # initialize the left and right bounds
        left = 1
        right = max(piles)

        while left < right:
            # get the middle index between left and right bounds indexes
            # hour_spent stands for the total hour koko spends
            middle = (left + right) // 2
            hour_spent = 0

            # iterate over the piles and calculate hour_spent
            # we increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)

            # check if middle is a workable speed, and cut the search space by half
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        # once the left and right boundaries coincide, we find the target value
        # that is, the minimum workable speed
        return right
