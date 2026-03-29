class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        tempRes = []
        def dfs(i):
            if i >= len(nums):
                res.append(tempRes[:])
                return
            
            tempRes.append(nums[i])
            dfs(i+1)
            tempRes.pop()
            dfs(i+1)
        dfs(0)
        return res
