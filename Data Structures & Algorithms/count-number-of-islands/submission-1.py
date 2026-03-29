class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        path = set()
        self.nbr_island = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == "0" or
                (r, c) in path
            ):
                return
            path.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in path:
                    self.nbr_island += 1
                    dfs(r, c)

        return self.nbr_island



            