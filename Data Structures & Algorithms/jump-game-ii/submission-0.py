class Solution:
    def jump(self, nums: List[int]) -> int:
        storeMin = [float('inf')]*len(nums)
        storeMin[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            for j in range(nums[i]+1):
                if i+ j >= len(nums):
                    continue
                storeMin[i] = min(storeMin[i],1+storeMin[j + i])
        return storeMin[0]
