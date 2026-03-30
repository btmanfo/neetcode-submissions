class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedStr = ""
        for i in range(max(len(word1), len(word2))):
            if i >= len(word1):
                mergedStr += word2[i:]
                return mergedStr
            if i >= len(word2):
                mergedStr += word1[i:]
                return mergedStr
            mergedStr += word1[i]
            mergedStr+= word2[i]
        return mergedStr