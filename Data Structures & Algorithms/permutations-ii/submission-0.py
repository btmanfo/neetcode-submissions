class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        setValue = set()

        def backPropragation(subset):
            if len(subset) == len(nums):
                setValue.add(tuple(subset))
                return
            for i in range(len(nums)):
                if nums[i] != float('-inf'):
                    subset.append(nums[i])
                    nums[i] = float('-inf')
                    backPropragation(subset)
                    nums[i] = subset[-1]
                    subset.pop()
        backPropragation([])
        return list(setValue)
            