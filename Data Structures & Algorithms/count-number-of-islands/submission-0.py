class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        island = 0
        ROWS = len(grid)
        COLUMS = len(grid[0])

        def dfs(i,j):
            if (i<0 or j<0 or i>= ROWS or j >=COLUMS or grid[i][j] == '0'):
                return
            grid[i][j] ='0'
            for position_x,position_y in directions:
                dfs(i+position_x, j +position_y)

        for i in range(ROWS):
            for j in range(COLUMS):
                if grid[i][j] == '1':
                    dfs(i,j)
                    island+=1
        return island
