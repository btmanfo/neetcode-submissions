class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        def dfs(i, target):
            #quand ton index est out of range tu va verifier si tu es arriver a la 
            #moitier
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            return dfs(i+1, target) or dfs(i+1, target - nums[i])
        return dfs(0, sum(nums)//2)