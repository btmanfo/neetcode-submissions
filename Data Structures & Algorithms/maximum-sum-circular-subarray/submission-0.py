class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxArray = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    total = 0
                    for w in range((i+j), (i+k+1)):
                        total += nums[(w%n)]
                    maxArray= max(maxArray, total)
        return maxArray