class CumstomStack:
    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.add = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top != len(self.stack) - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1

        ret = self.stack[self.top] + self.add[self.top]
        if self.top != 0:
            self.add[self.top - 1] += self.add[self.top]
        self.add[self.top] = 0
        self.top -= 1

        return ret

    def increment(self, k: int, val: int) -> None:
        lim = min(k - 1, self.top)
        if lim > 0:
            self.add[lim] += val


s = CumstomStack(12)
s.push(2)
s.pop()
print(s)