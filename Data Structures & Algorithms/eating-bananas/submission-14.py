class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles)
        leftPtr = 1
        res = maxValue

        while maxValue >= leftPtr:
            middlePtr = leftPtr + (maxValue - leftPtr) // 2

            totalCount = 0
            for i in piles:
                totalCount += math.ceil(i / middlePtr)

            if totalCount <= h:
                #il peut le manger dans le temps donner, donc on va voir sil y 
                #a pas un temps beaucoup plus rapide
                res = middlePtr
                maxValue = middlePtr - 1
            else:
                #elle ne peut pas finir de le manger avec le temps donner
                #donc il faut augmenter le nombre de banane manger
                leftPtr = middlePtr + 1

        return res