class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoint = []
        res = []

        for point in points:
            closestPoint.append([(point[0]*point[0]+point[1]*point[1]),point[0],point[1]])
        
        heapq.heapify(closestPoint)

        for i in range(k):
            res.append(heapq.heappop(closestPoint)[1:])
        return res


        