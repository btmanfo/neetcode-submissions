class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        theList = {}
        for i in range(len(nums)):
            theList[nums[i]] = i

        for i in range(len(nums)):
            newTarget = target - nums[i]

            if newTarget in theList and i != theList[newTarget]:
                return [i, theList[newTarget]]
        return [0,0]

