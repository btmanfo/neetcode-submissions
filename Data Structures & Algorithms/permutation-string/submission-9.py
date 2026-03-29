class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        firstString = [0]*26
        secondString = [0]*26

        for i in s1:
            firstString[ord(i) -ord('a')] +=1
        for i in range(len(s1)):
            secondString[ord(s2[i]) - ord('a')] +=1
        firstPtr = 0
        for r in range(len(s1), len(s2)):
            if firstString == secondString:
                return True
            secondString[ord(s2[firstPtr]) - ord('a')] -=1
            firstPtr +=1
            secondString[ord(s2[r])-ord('a')]  +=1
        return firstString == secondString
