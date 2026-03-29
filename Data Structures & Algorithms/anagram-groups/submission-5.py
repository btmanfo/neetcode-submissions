class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = defaultdict(list)
        for singleElement in strs:
            theWord =[0]*26
            for i in singleElement:
                theWord[ord(i)-ord('a')] +=1
            groupAnagrams[tuple(theWord)].append(singleElement)
            
        return list(groupAnagrams.values())