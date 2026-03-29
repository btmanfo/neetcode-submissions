class Solution:
    def minWindow(self, s: str, t: str) -> str:
        firstString = {}
        secondString = {}

        for i in t:
            firstString[i] = 1 + firstString.get(i,0)
        need = len(firstString)
        have = 0

        leftPtr = 0
        res = [-1,-1]
        resLen = float("infinity")

        for r in range(len(s)):
            secondString[s[r]] = 1+ secondString.get(s[r], 0)
            if s[r] in firstString and secondString[s[r]] == firstString[s[r]]:
                have +=1
            
            while have == need:
                if resLen > (r-leftPtr+1):
                    res = [leftPtr, r]
                    resLen = (r-leftPtr+1)
                secondString[s[leftPtr]] -=1
                if s[leftPtr] in firstString and firstString[s[leftPtr]]> secondString[s[leftPtr]]:
                    have-=1
                leftPtr+=1
        if resLen == float("infinity"):
            return ""
        else:
            return s[res[0]:res[1]+1]
