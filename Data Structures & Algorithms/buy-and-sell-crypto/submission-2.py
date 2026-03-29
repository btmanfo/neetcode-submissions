class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        x =0
        y=1
        result =0
        while(y<len(prices)):
            if(prices[y]-prices[x]<0):
                x+=1
                y= x+1
            elif(prices[y]-prices[x]>=0):
                if(result< (prices[y]-prices[x])):
                    result = prices[y]-prices[x]
                y+=1
        return result
        