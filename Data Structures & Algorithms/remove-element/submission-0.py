class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        totalCount = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            else:
                totalCount+=1
        return totalCount