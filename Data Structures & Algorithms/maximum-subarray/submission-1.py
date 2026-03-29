class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum <0:
                currentSum =0
            currentSum += num
            maxValue = max(maxValue, currentSum)
        return maxValue