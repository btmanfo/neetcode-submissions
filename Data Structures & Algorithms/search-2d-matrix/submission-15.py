class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rightArrayPtr = len(matrix)-1
        leftArrayPtr = 0

        arrayRes = -1
        while leftArrayPtr <= rightArrayPtr:
            middleArrayPtr = leftArrayPtr +(rightArrayPtr-leftArrayPtr)//2

            if matrix[middleArrayPtr][0]<=target<=matrix[middleArrayPtr][-1]:
                arrayRes = middleArrayPtr
                break
            elif matrix[middleArrayPtr][-1]< target:
                leftArrayPtr = middleArrayPtr +1
            elif matrix[middleArrayPtr][0]> target:
                rightArrayPtr = middleArrayPtr -1
            else:
                return False
        newRightPtr = len(matrix[0])-1
        newLeftPtr = 0
        while newRightPtr>=newLeftPtr:
            middlePtr = newLeftPtr +(newRightPtr-newLeftPtr)//2

            if matrix[arrayRes][middlePtr]<target:
                newLeftPtr = middlePtr +1
            elif matrix[arrayRes][middlePtr]>target:
                newRightPtr = middlePtr -1
            else:
                return True
        return False