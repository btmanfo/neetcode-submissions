class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largestArray = [-a for a in nums]
        heapq.heapify(largestArray)
        res = 0
        for i in range(k):
            res = heapq.heappop(largestArray)
        return -res