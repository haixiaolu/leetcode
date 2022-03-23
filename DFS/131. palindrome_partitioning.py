def partition(self, s):
    self.isPalindrome = lambda s: s == s[::-1]
    res = []
    self.backtrack(s, res, [])
    return res


def backtrack(self, s, res, path):
    if not s:
        res.append(path)
        return

    for i in range(1, len(s) + 1):
        if self.isPalindrome(s[:i]):
            self.backtrack(s[i:], res, path + [s[:i]])
