class MyHashMap:

    def __init__(self):
        self.value = []
        self.index = []

    def put(self, key: int, value: int) -> None:
        isExist = False
        position = 0
        for i in self.index:
            if i == key:
                self.value[position] = value
                isExist = True
            position +=1
        if isExist == False:
            self.value.append(value)
            self.index.append(key)

    def get(self, key: int) -> int:
        position = 0
        for i in self.index:
            if i == key:
                return self.value[position]
            position+=1
        return -1

    def remove(self, key: int) -> None:
        position = 0
        for i in self.index:
            if i == key:
                self.value[position] = None
                self.index[position] = None
            position +=1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)