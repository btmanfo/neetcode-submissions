class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(nums) or total> target:
                return
            cur.append(nums[i])
            #we dont want to add i+1 because it is possible we want to
            #add want to have the duplicate of the value til it begger than
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res


            