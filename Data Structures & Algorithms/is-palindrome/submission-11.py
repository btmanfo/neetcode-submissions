class Solution:
    def isPalindrome(self, s: str) -> bool:
        rightPtr = len(s)-1
        leftPtr = 0
        while rightPtr > leftPtr:
            while rightPtr>leftPtr and s[rightPtr].isalnum() == False:
                rightPtr-=1
            while rightPtr>leftPtr and s[leftPtr].isalnum() == False:
                leftPtr+=1
            if s[rightPtr].lower() != s[leftPtr].lower():
                return False
            rightPtr -=1
            leftPtr +=1
        return True
                
            