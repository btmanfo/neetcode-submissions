class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        res = []
        def dfs(r, c, i, theWord):
            if i == len(theWord):
                return True
            if (r>= ROWS or c >=COLS or r<0 or c<0 or theWord[i] != board[r][c]):
                return False
            board[r][c] = "*"
            res = (dfs(r-1, c, i+1, theWord) or dfs(r, c-1, i+1, theWord)
                    or dfs(r+1, c, i+1, theWord) or dfs(r, c+1, i+1, theWord))
            board[r][c] = theWord[i]
            return res
        for word in words:
            for r in range(ROWS):
                for c in range(COLS):
                    if dfs(r,c,0,word):
                        res.append(word)
        return res