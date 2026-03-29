class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        
        dist = {node: float("inf") for node in range(1,n+1)}

        def dfs(node, total_time_spend):
            if dist[node] <= total_time_spend:
                return
            dist[node] = total_time_spend

            for nei, time_spend in adj[node]:
                dfs(nei, total_time_spend+time_spend)
            
        dfs(k, 0)

        res = max(dist.values())
        return res if res<float("inf") else -1