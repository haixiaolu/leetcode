# leetcode 57. Insert Interval
"""
Given a list of non-overlapping intervals sort by their start time, insert a given interval at the correction 
position and merge all necessary intervals to product a list that has only mutually exclusively intervals
"""
"""
Approach:
1. skip all intervals which end before the start of the new interval, (intervals[i].end < newInterval.start)
2. Let's call the last interval 'b' that does not satisfy the above condition. if 'b' overlaps with the new 
   interval(a), b.start <= a.end, we need to merge them into a new interval 
"""


from numpy import insert


class Solution:
    def insert(self, intervals, newInterval):
        merged = []
        i, start, end = 0, 0, 0
        # skip ( and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with 'newInterval'
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        # insert the newInterval
        merged.append(newInterval)

        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged


def main():
    print(
        "Intervals after inserting the new interval: "
        + str(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    )
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    # print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()