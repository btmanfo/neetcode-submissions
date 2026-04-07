class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPtr = 0
        rightPtr = len(nums)-1
        middlePtr = 0
        while leftPtr <= rightPtr:
            middlePtr = leftPtr + math.floor((rightPtr - leftPtr)/2)
            if nums[middlePtr] > target:
                rightPtr = middlePtr -1
            elif nums[middlePtr]< target:
                leftPtr = middlePtr +1
            else:
                return middlePtr
        return -1
