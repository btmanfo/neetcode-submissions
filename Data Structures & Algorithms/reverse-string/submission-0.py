class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftPtr = 0
        rightPtr = len(s)-1

        while leftPtr < rightPtr:
            temp = s[leftPtr]
            s[leftPtr] = s[rightPtr]
            s[rightPtr] = temp
            leftPtr +=1
            rightPtr -=1