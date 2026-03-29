class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tableau ={}
        for i in nums:
            if i in tableau:
                tableau[i] = tableau[i]+1
            else:
                tableau[i] =1

        heap =[]
        for i in tableau.keys():
            heapq.heappush(heap, (tableau[i], i))
            if(len(heap)>k):
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res