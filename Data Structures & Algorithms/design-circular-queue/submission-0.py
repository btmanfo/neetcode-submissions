class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.arr) == self.k:
            return False
        else:
            self.arr.append(value)
            return True

    def deQueue(self) -> bool:
        newArr = []
        if len(self.arr) == 0:
            return False
        else:
            for i in range(len(self.arr)-1, 1):
                newArr.append(self.arr[i])
            self.arr = newArr
            return True

    def Front(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[0]

    def Rear(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]

    def isEmpty(self) -> bool:
        if self.arr == 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if len(self.arr) == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()