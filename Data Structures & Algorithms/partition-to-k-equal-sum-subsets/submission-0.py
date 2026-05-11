class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subset = [0]*k
        def backPropagation(i):
            if i == len(nums):
                for i in range(1, k):
                    if subset[i] != subset[i-1]:
                        return False
                return True
            for newTemp in range(k):
                subset[newTemp] += nums[i]
                if backPropagation(i+1):
                    return True
                subset[newTemp] -= nums[i]
            return False
        return backPropagation(0)