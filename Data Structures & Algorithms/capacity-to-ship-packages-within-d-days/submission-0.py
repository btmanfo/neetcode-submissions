class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minVal = max(weights)
        maxVal = sum(weights)
        res = maxVal
        while minVal <= maxVal:
            middleVal = minVal + math.floor((maxVal - minVal)/2)
            chip = 1
            totalSum = 0
            for weight in weights:
                if totalSum + weight > middleVal:
                    chip += 1
                    totalSum = weight
                else:
                    totalSum += weight
            if chip <= days:
                res = min(res, middleVal)
                maxVal = middleVal-1
            elif chip > days:
                minVal = middleVal +1
        return res

