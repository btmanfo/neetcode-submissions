class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPtr = 0
        rightPtr = 1
        maxValue = 0
        while rightPtr< len(prices):
            if (prices[leftPtr] - prices[rightPtr]) > 0:
                leftPtr = rightPtr
                rightPtr = leftPtr +1
            else:
                maxValue = max(maxValue, (prices[rightPtr] - prices[leftPtr]))
                rightPtr +=1
        
        return maxValue