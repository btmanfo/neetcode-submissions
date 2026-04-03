class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        totalTime = 1
        position = len(self.arr)-1
        while position >= 0 and self.arr[position] <= price:
            totalTime +=1
            position -=1
        self.arr.append(price)
        return totalTime


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)