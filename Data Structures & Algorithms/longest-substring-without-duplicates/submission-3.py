class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valeur =set()
        res =0
        l=0

        for i in range(len(s)):
            while s[i] in valeur:
                valeur.remove(s[l])
                l+=1
            valeur.add(s[i])
            res= max(res, i-l+1)
        return res
            
            