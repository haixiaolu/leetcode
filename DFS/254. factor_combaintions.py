"""
1. backtracking
- the idea is to iteratively divided the last number in the factor combo into smaller numbers
    - [12] - divided 12 by 2 -> [2, 6] -> divided 6 by 2 -> [2, 2, 3] -> 3 cannot divided by 2
    - [12] - divided 12 by 3 -> [3, 4] -> divide 4 by 2 -> [3, 2, 2] # duplicated
To fix the issure of duplicate, we pass the starting number for the factor search
    - if you've divided by 2, next try dividing by 2 or higher hence (2, 2, 3)
    - but if you now divide by 3, start the next division at 3
    - stop when i * i = num, because any number k > sqrt(num) == num/K < k (duplicate)
"""


def getFactors(n):
    res = []

    def dfs(cur, i):
        num = cur.pop()
        while i * i <= num:
            div = num // i
            if num % i == 0:
                res.append(cur + [i, div])
                dfs(cur + [i, div], i)
            i += 1

    dfs([n], 2)
    return res


print(getFactors(8))