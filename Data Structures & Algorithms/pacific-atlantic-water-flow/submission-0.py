class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = [[False]*len(heights[0]) for _ in range(len(heights))]
        atl = [[False]*len(heights[0]) for _ in range(len(heights))]
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(the_tableau, bool_tableau):
            q = deque(the_tableau)
            for r, c in the_tableau:
                bool_tableau[r][c] = True

            while q:
                r, c = q.popleft()
                for dx, dy in direction:
                    nx, ny = r + dx, c + dy
                    if (
                        nx < 0 or ny < 0 or nx >= ROWS or ny >= COLS or
                        bool_tableau[nx][ny] or
                        heights[nx][ny] < heights[r][c]
                    ):
                        continue
                    bool_tableau[nx][ny] = True
                    q.append((nx, ny))

        pacific = []
        atlantic = []

        for i in range(ROWS):
            pacific.append((i,0))
            atlantic.append((i,COLS-1))
        
        for i in range(COLS):
            pacific.append((0,i))
            atlantic.append((ROWS-1,i))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)
        res =[]
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res