class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)
        if len(self.arr) %2 != 0:
            return self.arr[math.floor(n/2)]
        return (self.arr[math.floor(n/2)]+self.arr[math.floor(n/2)-1])/2
        