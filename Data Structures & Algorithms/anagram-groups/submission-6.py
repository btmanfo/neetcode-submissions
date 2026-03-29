class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        theList = defaultdict(list)

        for i in strs:
            theTempList = [0]*26
            for j in i:
                theTempList[ord(j) - ord('a')] += 1
            theList[tuple(theTempList)].append(i)
        coolResult = []
        for j in theList.values():
            coolResult.append(j)
        return coolResult
