class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def hash(self, val):
        return val%self.size
        

    def add(self, key: int) -> None:
        i = self.hash(key)
        if key not in self.table[i]:
            self.table[i].append(key)
        

    def remove(self, key: int) -> None:
        i = self.hash(key)
        if key in self.table[i]:
            self.table[i].remove(key)

    def contains(self, key: int) -> bool:
        i = self.hash(key)
        return key in self.table[i]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)