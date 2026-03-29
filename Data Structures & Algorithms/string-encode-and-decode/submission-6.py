class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res+= str(len(i)) + "$" + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i<len(s):
            j = i

            while s[j] != "$":
                j+=1
            theSize = int(s[i:j])
            #12$aaaaaaaaaaaa5
            res.append(s[j+1:j+1+theSize])
            i = j+1+theSize
        return res
