class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(r,h,i):
            if i == len(word):
                return True
            if (r,h) in path or min(r,h) <0 or r >= len(board[0]) or h>= len(board):
                return False
            if board[h][r] != word[i]:
                return False
            
            path.add((r,h))
            res = dfs(r-1, h, i+1)or dfs(r+1,h, i+1)or dfs(r,h-1,i+1)or dfs(r, h+1, i+1)
            path.remove((r,h))
            return res
        for h in range(len(board)):
            for r in range(len(board[0])):
                if dfs(r,h,0):
                    return True
        return False