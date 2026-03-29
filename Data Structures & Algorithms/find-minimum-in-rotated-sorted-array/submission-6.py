class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(nums)-1

        res = nums[0]

        while leftPtr <= rightPtr:
            if nums[leftPtr] < nums[rightPtr]:
                res = min(res, nums[leftPtr])
                break
            middlePtr = leftPtr +(rightPtr- leftPtr)//2
            res = min(res, nums[middlePtr])

            if nums[middlePtr]>= nums[leftPtr]:
                leftPtr = middlePtr +1
            else:
                rightPtr = middlePtr -1
        return res