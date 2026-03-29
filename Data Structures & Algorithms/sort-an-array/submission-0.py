class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[j]< nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums