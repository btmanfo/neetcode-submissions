class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def dfs(i, m):
            if i == n and m == 0:
                return 0
            if i == n and m != 0:
                return float('inf')
            if i != m and m == 0:
                return float('inf')
            curSum = 0
            res = float('inf')
            for j in range(i, n-m+1):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j+1, m-1)))
            return res
        return dfs(0, k)