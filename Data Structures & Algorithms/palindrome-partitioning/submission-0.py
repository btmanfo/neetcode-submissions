class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #res will store all the arrays with palindrone line [["a","a","b"]]
        res = []
        #part will countain element that are palindrone ["a","a","b"]
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.isPalindrone(s,i,j) == True:
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res


    def isPalindrone(self,s,i,j) ->bool:
        while j>i:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True