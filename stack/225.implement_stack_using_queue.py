class MyStack:
    def __int__(self):
        self.queue = collections.queue()

    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

        def pop(self) -> int:
            return self.queue.popleft()

        def top(self) -> int:
            return self.queue[0]

        def empty(self) -> bool:
            return not self.queue