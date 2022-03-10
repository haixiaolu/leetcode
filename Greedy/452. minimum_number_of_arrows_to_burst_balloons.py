"""
1. Sort + greedy
   - sort the baloons by the end coordinate, and then check them one by one. 
     - check the first end point, then check the second and third start point
        --> if the second start coordinate smaller than the end point of the first one, it means it can be brusted
        --> if its larger than the end of the first point, it can't brust it 
"""


def findMinArrowShots(points):
    if not points:
        return 0

    # sort by x_end
    points.sort(key=lambda x: x[1])

    arrow = 1
    first_end = points[0][1]
    for x_start, x_end in points:
        # if the current balloon starts after the end of another one
        # one needs more arrow
        if first_end < x_start:
            arrow += 1
            first_end = x_end
    return arrow
