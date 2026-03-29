class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles)
        leftPtr = 1
        res = maxValue  # initialize with the highest possible speed

        while maxValue >= leftPtr:
            middlePtr = leftPtr + (maxValue - leftPtr) // 2

            totalCount = 0
            for i in piles:
                totalCount += math.ceil(i / middlePtr)

            if totalCount <= h:
                res = middlePtr  # this speed works, try a slower one
                maxValue = middlePtr - 1
            else:
                leftPtr = middlePtr + 1  # too slow, need higher speed

        return res