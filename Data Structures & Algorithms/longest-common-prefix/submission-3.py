class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        currentPrix = strs[0]
        for i in range(1, len(strs)):
            shortSize = min(len(currentPrix), len(strs[i]))
            tempSize = 0
            for j in range(0, shortSize):
                if currentPrix[j] != strs[i][j]:
                    break
                tempSize +=1
            currentPrix = currentPrix if len(currentPrix) < tempSize else currentPrix[:tempSize]
        return currentPrix
                