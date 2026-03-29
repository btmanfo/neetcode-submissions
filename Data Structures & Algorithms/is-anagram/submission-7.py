class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        firstString = {}
        secondString ={}

        for i in s:
            if i in firstString:
                firstString[i] +=1
            else:
                firstString[i] =1
        for i in t:
            if i in secondString:
                secondString[i] += 1
            else:
                secondString[i] =1
        return firstString == secondString