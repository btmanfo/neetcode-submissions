class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubArray = float('inf')
        leftPtr = 0
        rightPtr = 0
        totalSum = 0

        while rightPtr <= len(nums)-1:
            totalSum += nums[rightPtr]
            while totalSum >= target:
                minSubArray = min(minSubArray,(rightPtr-leftPtr)+1)
                totalSum -= nums[leftPtr]
                leftPtr+=1
            rightPtr += 1
        return minSubArray if minSubArray != float('inf') else 0