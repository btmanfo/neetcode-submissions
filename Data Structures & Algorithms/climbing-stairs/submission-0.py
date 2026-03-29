class Solution:
    def climbStairs(self, n: int) -> int:
        self.number_combination = 0
        def dfs(i):
            if i == n:
                self.number_combination = self.number_combination +1
            if i>n:
                return
            dfs(i+1)
            dfs(i+2)
        dfs(0)
        return self.number_combination