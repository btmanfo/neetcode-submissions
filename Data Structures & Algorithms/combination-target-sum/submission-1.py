class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        tempRes = []

        def dfs(i, totalSum):
            if i >= len(nums):
                return
            if totalSum == target:
                res.append(tempRes[:])
                return
            if totalSum > target:
                return
            tempRes.append(nums[i])
            dfs(i, totalSum + nums[i])
            tempRes.pop()
            dfs(i+1, totalSum)
        dfs(0,0)
        return res