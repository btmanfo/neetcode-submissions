class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        colum = collections.defaultdict(set)
        box =  collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in row[i] or
                        board[i][j] in colum[j] or
                        board[i][j] in box[(i // 3, j // 3)]):
                    return False
                row[i].add(board[i][j])
                colum[j].add(board[i][j])
                box[(i // 3, j // 3)].add(board[i][j])

        return True
