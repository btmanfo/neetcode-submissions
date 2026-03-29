class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, [])
        leftPtr = 0
        rightPtr = len(values)-1
        while rightPtr>= leftPtr:
            middlePtr = leftPtr +(rightPtr-leftPtr)//2

            if values[middlePtr][1] <= timestamp:
                res = values[middlePtr][0]
                leftPtr = middlePtr +1
            elif values[middlePtr][1]> timestamp:
                rightPtr = middlePtr -1
        return res
