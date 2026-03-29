class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        values = [-s for s in nums]
        heapq.heapify(values)
        maxSize = k
        res = 0
        while maxSize >0:
            if maxSize == 1:
                res = -heapq.heappop(values)
            else:
                heapq.heappop(values)
            maxSize -=1
        return res