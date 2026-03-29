class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        remaining_fuit = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    remaining_fuit +=1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and remaining_fuit>0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dx, dy in direction:
                    new_r = r +dx
                    new_c = c + dy
                    if (new_c<0 or new_r<0 or new_c>=COLS or new_r >= ROWS or grid[new_r][new_c] !=1):
                        continue
                    grid[new_r][new_c] = 2
                    q.append([new_r, new_c])
                    remaining_fuit-=1
            time+=1
        return time if remaining_fuit ==0 else -1

