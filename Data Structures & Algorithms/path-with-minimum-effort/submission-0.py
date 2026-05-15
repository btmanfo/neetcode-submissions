class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Quand on cherche a minimiser le cout dans un arbre de recherche, il est toujours meilleur de
        # passer par Dijkstra's Algorithm
        ROWS = len(heights)
        COLS = len(heights[0])
        minHeap = [[0,0,0]]
        visit = set()
        direction = [[1,0], [0,1], [-1, 0], [0,-1]]

        while minHeap:
            diff, x, y = heapq.heappop(minHeap)

            if (x,y) in visit:
                continue
            visit.add((x,y))

            if (x,y) == (ROWS-1, COLS-1):
                return diff

            for dx, dy in direction:
                newX = dx + x
                newY = dy + y

                if (newX >= ROWS or newY >= COLS or newX < 0 or newY < 0 or (newX, newY) in visit):
                    continue
                # On cherche a minimiser le plus grand effort pour passer dun point a un autre.
                newDiff = max(diff, abs(heights[x][y] - heights[newX][newY]))
                heapq.heappush(minHeap, [newDiff, newX, newY])
        return 0