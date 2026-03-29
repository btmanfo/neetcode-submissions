class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        #this is used to store our element and avoid revisiting elements
        #that were visited
        path = set()

        def dfs(theRow, theColumn, i):
            #this means that we found the word
            if i == len(word):
                return True
            #if it out of bounce we return false
            #if it is a caracter that we are not looking for we return false
            #if we already looked at the value we return false
            if(theRow<0 or theColumn<0 or theRow>= rows or theColumn>=cols
            or word[i] != board[theRow][theColumn]
            or (theRow, theColumn) in path):
                return False

            #so now we get the correct value and we add
            path.add((theRow, theColumn))
            #now we are going to run it on all adjacent column
            res = dfs(theRow +1, theColumn, i+1) or dfs(theRow, theColumn+1, i+1) or dfs(theRow -1, theColumn, i+1) or dfs(theRow, theColumn-1, i+1)
            path.remove((theRow, theColumn))
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False

