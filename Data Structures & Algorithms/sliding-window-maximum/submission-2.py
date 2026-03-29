class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        theSet = {}
        res = []

        for i in range(k):
            theSet[i]= nums[i]
        res.append(max(theSet.values()))
        leftPtr = 0
        for r in range(k, len(nums)):
            theSet[r]=nums[r]
            theSet[leftPtr] = float('-inf')
            leftPtr+=1
            res.append(max(theSet.values()))
        return res