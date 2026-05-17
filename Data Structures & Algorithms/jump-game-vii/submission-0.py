class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        def dfs(i):
            if i == n-1:
                return True
            if i >= n:
                return False
            if s[i] == 1:
                return False
            for j in range(i+minJump, i+maxJump):
                if dfs(j):
                    return True
            return False
        return dfs(0)