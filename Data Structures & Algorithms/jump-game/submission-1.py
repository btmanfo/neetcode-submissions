class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) -1:
                return True
            
            if nums[i] == 0:
                return False
            
            maxValue = min(len(nums), i+nums[i]+1)

            for j in range(i+1, maxValue):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)