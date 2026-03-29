class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = 0
        for i in piles:
            maxSpeed = max(maxSpeed, i)
        leftPtr = 1
        rightPtr = maxSpeed
        minSpeed = maxSpeed
        while leftPtr<= rightPtr:
            middlePtr = leftPtr + (rightPtr -leftPtr)//2

            numberOfTime = 0

            for i in piles:
                numberOfTime += math.ceil(i/middlePtr)
            if numberOfTime > h:
                leftPtr = middlePtr + 1
            elif numberOfTime <= h:
                minSpeed = middlePtr
                rightPtr = middlePtr -1
        return minSpeed