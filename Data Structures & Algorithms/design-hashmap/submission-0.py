class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
        
    def hash(self, val):
        return val%self.size

    def put(self, key: int, val: int) -> None:
        i = self.hash(key)
        for k, v in self.table[i]:
            if k==key:
                self.table[i].remove((k, v))
                break
        
        self.table[i].append((key, val))

        
        

    def get(self, key: int) -> int:
        i = self.hash(key)
        for k,v in self.table[i]:
            if k==key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        i = self.hash(key)
        for k, v in self.table[i]:
            if k==key:
                self.table[i].remove((k, v))
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)