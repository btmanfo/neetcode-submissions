class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        values = []

        for x,y in points:
            tempValues = [((x-0)**2 + (y-0)**2)**(1/2), x, y]
            values.append(tempValues)
        heapq.heapify(values)
        res = []
        maxSize = k
        while maxSize > 0:
            tempValue = heapq.heappop(values)
            res.append([tempValue[1], tempValue[2]])
            maxSize -=1
        return res