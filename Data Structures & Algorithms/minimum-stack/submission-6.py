class MinStack:

    def __init__(self):
        self.myArray = []
        self.minArray =[]

    def push(self, val: int) -> None:
        self.myArray.append(val)
        if(self.minArray):
            val = min(val, self.minArray[-1])
        self.minArray.append(val)

    def pop(self) -> None:
        self.minArray.pop()
        self.myArray.pop()

    def top(self) -> int:
        return self.myArray[-1]

    def getMin(self) -> int:
        return self.minArray[-1]
