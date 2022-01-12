class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k  # 固定大小的数组
        self.head_index = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        # 如果队列是满的， return False
        if self.count == self.capacity:
            return False

        self.queue[(self.head_index + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.head_index + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


obj = MyCircularQueue(3)
print(obj.enQueue(3))
print(obj.enQueue(2))
print(obj.deQueue())
print(obj.isEmpty())
print(obj.isFull())