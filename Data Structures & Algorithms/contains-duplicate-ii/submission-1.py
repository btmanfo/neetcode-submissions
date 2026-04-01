class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mb = {}
        for i in range(len(nums)):
            if nums[i] in mb and abs(i- mb[nums[i]]) <= k:
                return True
            mb[nums[i]] = i
        return False