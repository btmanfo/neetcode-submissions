class Solution:
    def placeInOrder(self, value):
        table = [0]*26
        returnValue = ''
        for i in value:
            table[ord(i)- ord('a')] += 1
        for i in range(26):
            if table[i] > 0:
                tempVal = (chr(i) *table[i])
                returnValue += tempVal
        return returnValue
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allValue = defaultdict(list)

        for currChar in strs:
            currCharacter = self.placeInOrder(currChar)
            allValue[currCharacter].append(currChar)
        return list(allValue.values())