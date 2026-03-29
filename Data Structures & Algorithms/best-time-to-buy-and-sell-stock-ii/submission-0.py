class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalPrice = 0
        for i in range(1,len(prices)):
            subtotal = prices[i] - prices[i-1]
            if subtotal >0:
                totalPrice += subtotal
        return totalPrice
                