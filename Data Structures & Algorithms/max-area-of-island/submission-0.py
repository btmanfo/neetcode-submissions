class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        self.number_of_1 = 0
        max_island_size = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(i,j):
            if i<0 or j<0 or i>= ROWS or j>= COLUMNS or grid[i][j] == 0:
                return
            
            self.number_of_1+=1
            grid[i][j] = 0

            for position_x, position_y in directions:
                dfs(i+position_x, j+position_y)
        
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    dfs(i,j)
                    max_island_size = max(max_island_size, self.number_of_1)
                    self.number_of_1 =0
        return max_island_size
            