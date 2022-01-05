class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.is_empty())
s.push(2)
print(s.is_empty())
s.push("dog")
print(s.peek())
print(s.size())
s.pop()
print(s.peek())
s.pop()
print(s.size())