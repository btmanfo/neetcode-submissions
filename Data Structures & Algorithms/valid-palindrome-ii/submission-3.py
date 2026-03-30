class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr =  len(s)-1
        isSkip = False
        while leftPtr < rightPtr:
            if s[leftPtr] != s[rightPtr]:
                if isSkip == False:
                    #check left
                    if s[leftPtr+1] == s[rightPtr]:
                        isSkip = True
                        leftPtr +=1
                        continue
                    #check right
                    if s[leftPtr] == s[rightPtr -1]:
                        isSkip = True
                        rightPtr -=1
                        continue
                    #skip both
                    if s[leftPtr+1] == s[rightPtr-1]:
                        isSkip = True
                        rightPtr -=1
                        lefPtr +=1
                        continue
                return False
            leftPtr +=1
            rightPtr -=1
        return True