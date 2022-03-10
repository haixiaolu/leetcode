"""
1. Using Greedy Approach based on Starting points
  
    - if we sort the given intervals based on starting points, the greedy approach works very well. 
    - while considering the intervals in the ascending order of starting points, we make use of a pointer "Prev"
      pointer to keep track of the interval just included in the final list. 
    - While traversing, we can encounter 3 possibilities: 
    1): The two intervals currently considered are non-overlapping
    2): The two intervals currently considered are overlapping and the end point of the later interval falls 
        before the end point of the previous interval 
    3):The twp intervals currently considered are overlapping the later intervals falls after the end point of the previous interval
"""


def eraseOverlapIntervals(intervals):
    intervals.sort()

    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)
    return res


print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
