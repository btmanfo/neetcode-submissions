class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPtr =0
        rightPtr = len(nums)-1
        middlePtr = 0
        while( leftPtr <= rightPtr):
            middlePtr = leftPtr + (rightPtr - leftPtr) // 2
            if nums[middlePtr] > target:
                rightPtr = middlePtr -1
            if nums[middlePtr]< target:
                leftPtr = middlePtr +1
            if nums[middlePtr] == target:
                return middlePtr
        return -1
            