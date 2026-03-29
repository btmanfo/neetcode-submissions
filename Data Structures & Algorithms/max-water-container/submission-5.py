class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sizeContainer =0
        pointerLeft = len(heights)-1
        i =0
        while(pointerLeft>i):
            potentielSize = (pointerLeft-i) * min(heights[i],heights[pointerLeft])
            if(potentielSize>sizeContainer):
                sizeContainer = potentielSize
            if(heights[i]>=heights[pointerLeft]):
                pointerLeft-=1
            if(heights[i]<heights[pointerLeft]):
                i+=1
            
        return sizeContainer
        
        