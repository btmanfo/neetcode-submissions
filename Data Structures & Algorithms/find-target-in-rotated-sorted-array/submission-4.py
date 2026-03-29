class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPtr = 0
        rightPtr = len(nums)-1
        res = -1
        while leftPtr <= rightPtr:
            middlePtr = leftPtr + (rightPtr - leftPtr)//2
            if nums[middlePtr] == target:
                res = middlePtr
                break
            elif nums[middlePtr] >= nums[leftPtr]:
                if target <= nums[middlePtr] and target >= nums[leftPtr]:
                    rightPtr = middlePtr -1
                else:
                    leftPtr = middlePtr +1
            else:
                if target>= nums[middlePtr] and target <= nums[rightPtr]:
                    leftPtr = middlePtr +1
                else:
                    rightPtr = middlePtr- 1

        return res