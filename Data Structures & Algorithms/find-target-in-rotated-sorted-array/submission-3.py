class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPtr =0
        rightPtr = len(nums)-1
        res = -1

        while rightPtr >= leftPtr:
            middlePtr = leftPtr + (rightPtr - leftPtr)//2
            if nums[middlePtr] == target:
                res = middlePtr
                break
            if nums[leftPtr]<= nums[middlePtr]:
                if nums[leftPtr]<= target <= nums[middlePtr]:
                    rightPtr = middlePtr -1
                else:
                    leftPtr = middlePtr +1
            else:
                if nums[middlePtr] <= target <= nums[rightPtr]:
                    leftPtr = middlePtr +1
                else:
                    rightPtr = middlePtr -1
        return res


        return res

