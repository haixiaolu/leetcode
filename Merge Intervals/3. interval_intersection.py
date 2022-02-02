# leetcode 986.Interval List Intersection
"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals
sorted on their start time
"""
"""
Approach:
iterate through both the lists together to see if any two intervals overlap. if two intervals overlap, we will
insert the overlapped part into a result list and move on to the next interval which is finishing early
"""


class Solution:
    def intervalIntersection(self, firstList, secondList):
        result = []
        i, j, start, end = 0, 0, 0, 1
        while i < len(firstList) and j < len(secondList):
            # check if intervals overlap and firstList's start time lies with the secondList
            first_overlap_second = (
                firstList[i][start] >= secondList[j][start]
                and firstList[i][start] <= secondList[j][end]
            )

            # check if intervals overlap and firstList's start lies with the secondList
            second_overlap_first = (
                secondList[j][start] >= firstList[i][start]
                and secondList[j][start] <= firstList[i][end]
            )

            # store the intersection part
            if first_overlap_second or second_overlap_first:
                result.append(
                    [
                        max(firstList[i][start], secondList[j][start]),
                        min(firstList[i][end], secondList[j][end]),
                    ]
                )
            # move next from the interval which is finishing first
            if firstList[i][end] < secondList[j][end]:
                i += 1
            else:
                j += 1
        return result
