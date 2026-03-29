class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            #si on le met avant on risque peut etre detre out of range. Avec le cas
            #de base on evite cela (if i in dp)
            if s[i] == '0':
                return 0

            rep = dfs(i+1)
            if i < len(s) -1:
                if(s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                    rep += dfs(i+2)
            dp[i] = rep
            return rep
        return dfs(0)
