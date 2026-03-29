class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        allStones = [-a for a in stones]
        heapq.heapify(allStones)
        while len(allStones) > 1:
            fistValue = -heapq.heappop(allStones)
            secondValue = -heapq.heappop(allStones)
            if fistValue == secondValue:
                continue
            if fistValue < secondValue:
                newValue = secondValue - fistValue
                heapq.heappush(allStones,-newValue)
            if fistValue > secondValue:
                newValue = fistValue - secondValue
                heapq.heappush(allStones,-newValue)
        return -allStones[0] if allStones else 0