def sqrt(x):
    if not x:
        return

    left, right = 0, max(1, x)
    while right - left > 1e-10:
        mid = (left + right) / 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid
        else:
            right = mid
    return left


print(sqrt(4))