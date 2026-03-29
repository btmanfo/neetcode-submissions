class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftPtr = 0
        rightPtr = len(matrix) -1
        middlePtr = 0
        while(leftPtr <= rightPtr):
            middlePtr = leftPtr + (rightPtr -leftPtr)//2
            if(matrix[middlePtr][0]<= target<= matrix[middlePtr][-1]):
                break;
            if(matrix[middlePtr][0]> target):
                rightPtr = middlePtr-1
            if(matrix[middlePtr][-1]< target):
                leftPtr = middlePtr+1
        
        rightColumnPtr = len(matrix[0]) -1
        leftColumnPtr =0
        middlColmnPtr = 0

        while(rightColumnPtr>= leftColumnPtr):
            middlColmnPtr = leftColumnPtr + (rightColumnPtr-leftColumnPtr)//2
            if(matrix[middlePtr][middlColmnPtr]> target):
                rightColumnPtr = middlColmnPtr -1
            if(matrix[middlePtr][middlColmnPtr]< target):
                leftColumnPtr = middlColmnPtr+1
            if(matrix[middlePtr][middlColmnPtr]== target):
                return True
        return False
            
