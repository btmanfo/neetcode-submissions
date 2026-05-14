class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj =[[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def dfs(node, parent):
            maxValue = 0
            for i in adj[node]:
                if i == parent:
                    continue
                maxValue = max(maxValue, 1+ dfs(i, node))
            return maxValue
        maxHeight = n
        res = []
        for i in range(n):
            height = dfs(i, -1)
            if height == maxHeight:
                res.append(i)
            elif height < maxHeight:
                maxHeight = height
                res = [i]
        return res

                

                