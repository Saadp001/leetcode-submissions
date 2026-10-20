class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        adj = [[] for _ in range(n+1)]

        for i, j, w in times:
            adj[i].append((j, w))

        dist = [float('inf')]*(n+1)

        dist[k] = 0
        h = []
        heapq.heappush(h, (0, k))
        

        while h:
            
            dis, node = heapq.heappop(h)

            if dis > dist[node]:
                continue

            for nei, di in adj[node]:
                new_dis = di + dis

                if new_dis < dist[nei]:
                    dist[nei] = new_dis
                    heapq.heappush(h, (new_dis, nei))

        maxi = max(dist[1:])

        return maxi if maxi != float('inf') else -1            