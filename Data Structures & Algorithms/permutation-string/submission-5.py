class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        s1HashMap = {}
        s2HashMap ={}
        for i in s1:
            s1HashMap[i] = 1+ s1HashMap.get(i, 0);

        leftPtr =0
        for i in range(len(s1)):
            s2HashMap[s2[i]] = 1+ s2HashMap.get(s2[i], 0);
        if(s1HashMap == s2HashMap):
            return True
        
        for i in range(len(s1), len(s2), 1):
            s2HashMap[s2[i]] = 1+ s2HashMap.get(s2[i], 0)
            s2HashMap[s2[leftPtr]] -= 1
            if(s2HashMap[s2[leftPtr]] == 0):
                s2HashMap.pop(s2[leftPtr])
            leftPtr+=1
            if(s1HashMap == s2HashMap):
                return True
        return False