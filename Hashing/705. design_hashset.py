# 超大数组 （不考虑空间的话）
class MyHashSet:
    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key: int):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]


# 拉链法
class MyHashSet:
    def __init__(self):
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hashing(self, key):
        return key % self.buckets

    def position(self, key):
        return key // self.buckets

    def add(self, key):
        hashkey = self.hashing(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.position(key)] = 1

    def remove(self, key):
        hashkey = self.hashing(key)
        if self.table[hashkey]:
            self.table[hashkey][self.position(key)] = 0

    def contains(self, key):
        hashkey = self.hashing(key)
        return (self.table[hashkey] != []) and (
            self.table[hashkey][self.position(key)] == 1
        )
