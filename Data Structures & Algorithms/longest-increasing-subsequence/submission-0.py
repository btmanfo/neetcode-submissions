class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.maxLength = 0

        def dfs(prev, index, count):
            self.maxLength = max(self.maxLength, count)
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if nums[i] > prev:
                    dfs(nums[i], i + 1, count + 1)
                else:
                    dfs(prev, i + 1, count)

        dfs(float('-inf'), 0, 0)
        return self.maxLength