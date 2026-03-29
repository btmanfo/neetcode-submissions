class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        longestSubString = 0
        while i<len(s):
            j =i
            theSet = set()
            nbrOfCharacter = 0

            while j<len(s) and s[j] not in theSet:
                theSet.add(s[j])
                nbrOfCharacter+=1
                j+=1
            longestSubString = max(longestSubString,nbrOfCharacter )
            i+=1
        return longestSubString
            