class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        len_x_axis = len(grid)
        len_y_axis = len(grid[0])
        N=len(grid)

        the_min_heap= [[grid[0][0],0,0]]
        seen.add((0,0))
        while the_min_heap:
            elevation, x,y = heapq.heappop(the_min_heap)
            if x==N-1 and y == N-1:
                return elevation
            for i,j in direction:
                adj_x = x+i
                adj_y = y+j

                if(adj_x<0 or adj_y<0 or adj_x == N or adj_y == N or (adj_x,adj_y)in seen):
                    continue
                seen.add((adj_x, adj_y))
                heapq.heappush(the_min_heap, [max(elevation, grid[adj_y][adj_x]), adj_x,adj_y])
                