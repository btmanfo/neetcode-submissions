class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        tempRes = []

        def dfs(i, total):
            if total == target:
                res.append(tempRes[:])
                return
            if total > target:
                return
            if i >= len(candidates):
                return
            
            tempRes.append(candidates[i])
            dfs(i+1, total+ candidates[i])
            tempRes.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, total)
            #11234
        dfs(0,0)
        return res