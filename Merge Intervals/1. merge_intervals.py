# leetcode 56.Merge Intervals
"""
Given a list of intervals, merge all the overlapping intervals to 
produce a list that has only mutually exclusive intervals
"""
"""
Approach:
1. Sort the intervals on the start time to ensure a.start <= b.start
2. if a overlaps b (b.start < a.end), we need to merge them into a new interval
3. We will keep repeating the above two steps to merge c with the next interval if it overlaps with c
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def merge(intervals):
        if len(intervals) < 2:
            return intervals

        # sort the intervals on the start time
        intervals.sort(key=lambda x: x.start)
        merged_intervals = []
        start = intervals[0].start
        end = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if intervals.start <= end:  # overlapping intervals, adjust the 'end'
                end = max(interval.end, end)
            else:  # non-overlapping interval, add the previous interval and reset
                merged_intervals.append(Interval(start, end))
                start = interval.start
                end = interval.end

        # add the last interval
        merged_intervals.append(Interval(start, end))
        return merged_intervals
