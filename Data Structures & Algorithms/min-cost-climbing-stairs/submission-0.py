class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            #when we will out of bounce we will just return 0 so it cost[1]+0
            if i>= len(cost):
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))
        return min(dfs(0), dfs(1))