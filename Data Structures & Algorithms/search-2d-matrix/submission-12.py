class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            middlePtr = 0;
            rightPtr = len(i)-1;
            leftPtr = 0

            while(leftPtr<= rightPtr):
                middlePtr = leftPtr +( rightPtr - leftPtr)//2
                if(i[middlePtr]> target):
                    rightPtr = middlePtr -1
                if(i[middlePtr]< target):
                    leftPtr = middlePtr +1
                if(i[middlePtr] == target):
                    return True
        return False