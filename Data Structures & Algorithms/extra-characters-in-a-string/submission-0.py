class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        setValue = set(dictionary)
        validIndex = [0]*len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in setValue:
                    for k in range(i, j+1):
                        validIndex[k] =1
        res = 0
        for i in validIndex:
            if i == 0:
                res +=1
        return res