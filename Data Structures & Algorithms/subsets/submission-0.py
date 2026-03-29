class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tempValue = []

        def dfs(i):
            if i >= len(nums):
                res.append(tempValue[:])
                return
            tempValue.append(nums[i])
            dfs(i+1)
            tempValue.pop()
            dfs(i+1)
        dfs(0)
        return res