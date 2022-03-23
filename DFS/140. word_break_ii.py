def wordBreak(s, wordDict):
    ans = []
    n = len(s)

    def backtrack(temp, start):
        if start == n:
            ans.append(temp[1:])

        for i in range(start, n):
            if s[start : i + 1] in wordDict:
                backtrack(temp + "" + s[start : i + 1], i + 1)

    backtrack("", 0)
    return ans
