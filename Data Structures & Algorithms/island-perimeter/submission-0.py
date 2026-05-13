class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i,j):
            # Donc je va envoyer la valeur 1 quand le prochaine cellule est le vide ou de leau
            if i<0 or j<0 or i>= rows or j>= cols or grid[i][j] == 0:
                return 1
            #Si on a deja vu la cellule alors on evite toujour du aller encore
            if (i, j) in visit:
                return 0
            visit.add((i,j))
            perim = dfs(i,j+1) + dfs(i+1,j) + dfs(i-1, j) + dfs(i, j-1)
            return perim
        for i in range(rows):
            for j in range(cols):
                # Il faut juste que juste une coordonner dune bonne ile
                if grid[i][j]:
                    return dfs(i,j)