class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSize = float('-inf')
        for i in range(len(nums)):
            subtotal = 0
            for j in range(i, len(nums)):
                subtotal+= nums[j]
                maxSize = max(maxSize, subtotal)
        return maxSize