class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        idxValue = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def backTrack(i, theCursor):
            if len(theCursor) == len(digits):
                res.append(theCursor)
                return
            
            for j in idxValue[digits[i]]:
                backTrack(i+1, theCursor+j)
        if digits:
            backTrack(0, "")
        return res
