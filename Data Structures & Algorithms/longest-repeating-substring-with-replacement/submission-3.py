class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={}
        leftPtr = 0
        res =0
        for rightPtr in range(len(s)):
            count[s[rightPtr]] = 1+ count.get(s[rightPtr], 0)
            while((rightPtr-leftPtr+1)-max(count.values())> k):
                count[s[leftPtr]] -=1
                leftPtr+=1
            res = max(res, rightPtr-leftPtr+1)
        return res