class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtracking(curr, i):
            if i == len(nums):
                res.add(tuple(curr))
                return
            curr.append(nums[i])
            backtracking(curr, i+1)
            curr.pop()
            backtracking(curr, i+1)
        nums.sort()
        backtracking([], 0)
        return [list(theValue) for theValue in res]


            