class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        hashDict = set(dictionary)
        storeState = {len(s):0}
        def dfs(i):
            if i == len(s):
                return 0
            if i in storeState:
                return storeState[i]
            res = 1+ dfs(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in hashDict:
                    res = min(res, dfs(j+1))
            storeState[i] = res
            return res
        return dfs(0)