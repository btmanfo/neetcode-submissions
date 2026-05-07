class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        arr = [[-theFreq, theValue] for theValue, theFreq in freq.items()]
        heapq.heapify(arr)

        temp = []
        res = ""
        while temp or arr:
            if temp and not arr:
                return ""
            newFrq, newValue = heapq.heappop(arr)
            res+=newValue
            newFrq += 1

            if temp:
                heapq.heappush(arr, temp)
                temp = None
            if newFrq != 0:
                temp = [newFrq, newValue]
        return res
