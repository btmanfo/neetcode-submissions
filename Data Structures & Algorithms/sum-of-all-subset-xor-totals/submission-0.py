class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtracking(i, subset):
            nonlocal res
            xor = 0
            for j in subset:
                xor ^= j
            res += xor

            for m in range(i, len(nums)):
                subset.append(nums[m])
                backtracking(m+1, subset)
                subset.pop()
        backtracking(0, [])
        return res