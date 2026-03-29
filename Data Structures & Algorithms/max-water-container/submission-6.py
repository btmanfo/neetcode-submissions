class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(heights) -1

        max_area = 0
        while leftPtr < rightPtr:
            x_axis =  rightPtr - leftPtr
            y_axis = min(heights[leftPtr], heights[rightPtr])

            max_area = max(max_area, (x_axis * y_axis))

            if heights[leftPtr] >= heights[rightPtr]:
                rightPtr -=1
            if heights[leftPtr]< heights[rightPtr]:
                leftPtr +=1
        return max_area