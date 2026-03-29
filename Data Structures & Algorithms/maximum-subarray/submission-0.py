class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_final = float('-inf')

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                sum_final = max(current_sum, sum_final)
        return sum_final