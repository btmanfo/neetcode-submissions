class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(x,y):
            if x>n-1 or y>m-1:
                return 0
            if x == n-1 and y == m-1:
                return 1
            
            return  dfs(x + 1, y) + dfs(x, y + 1)
        return dfs(0,0)

