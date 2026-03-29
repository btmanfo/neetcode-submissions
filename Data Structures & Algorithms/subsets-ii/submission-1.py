class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i, total:list):
            if i == len(nums):
                res.add(tuple(total))
                return
            
            total.append(nums[i])
            dfs(i+1, total)
            total.pop()
            dfs(i+1, total)
        nums.sort()
        dfs(0, [])

        return [list(a) for a in res]
            