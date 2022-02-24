# 超大数组
class MyHashMap:
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map[key]

    def remove(self, key):
        self.map[key] = -1


# 拉链法
class MyHashMap:
    def __init__(self):
        self.buckets = 1009  # 1009 是1000以后的第一个质数
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key, value):
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key):
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key):
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return
