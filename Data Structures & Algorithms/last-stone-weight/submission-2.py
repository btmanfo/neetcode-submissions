class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.values = [-s for s in stones]

        heapq.heapify(self.values)
        while len(self.values) > 1:
            x = abs(heapq.heappop(self.values))
            y = abs(heapq.heappop(self.values))

            if x != y:
                heapq.heappush(self.values, y-x)
        self.values.append(0)
        return abs(self.values[0])

