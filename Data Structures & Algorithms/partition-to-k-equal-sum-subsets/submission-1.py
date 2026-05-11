class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total %k != 0:
            return False
        nums.sort(reverse= True)
        target = math.floor(total/k)
        used  = [False] * len(nums)

        def backTrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backTrack(0, k-1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j]> target:
                    continue
                used[j] = True
                if backTrack(j+1, k, subsetSum + nums[j]):
                    return True
                used[j]= False
                if subsetSum == 0: # Pruning
                    return False

            return False

        return backTrack(0, k, 0)