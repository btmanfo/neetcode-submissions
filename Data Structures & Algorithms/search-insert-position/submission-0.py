class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leftPtr = 0
        rightPtr = len(nums)-1
        while leftPtr <= rightPtr:
            self.middlePtr = leftPtr + math.floor((rightPtr - leftPtr)/2)
            if nums[self.middlePtr] > target:
                rightPtr = self.middlePtr -1
            elif nums[self.middlePtr] < target:
                leftPtr = self.middlePtr +1
            else:
                return self.middlePtr
        return self.middlePtr +1