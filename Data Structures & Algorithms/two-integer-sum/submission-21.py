class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newElement = {}

        for i in range(len(nums)):
            newElement[nums[i]] = i

        for i in range(len(nums)):
            targetInString = target -nums[i]
            if targetInString in newElement and i != newElement[targetInString] :
                return [i, newElement[targetInString]]
        return [0,0]
