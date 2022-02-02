# leetcode 252. meeting rooms
"""
Given an array of intervals representing 'N' appointments, find out if a person can attend all the appointments
"""
"""Approach:
We can sort all the intervals by start time and then check if any two intervals overlap. A person will not be 
able to attend all appointment if any two appointment overlap
"""


def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i - 1][end]:
            return False
    return True
