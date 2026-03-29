class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s):True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for j in wordDict:
                if ((i+len(j))<= len(s) and s[i: i+ len(j)] == j):
                    if dfs(i+len(j)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)