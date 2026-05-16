class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        globalMax = nums[0]

        for i in range(n):
            curr_sum = 0
            for j in range(i, i+n):
                curr_sum += nums[j%n]
                globalMax = max(globalMax, curr_sum)
        return globalMax