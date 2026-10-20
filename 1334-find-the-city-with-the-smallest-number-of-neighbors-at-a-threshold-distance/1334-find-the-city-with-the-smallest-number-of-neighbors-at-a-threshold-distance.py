class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        
        adj = [[] for _ in range(n)]

        for i, j, w in edges:
            adj[i].append((j,w))
            adj[j].append((i,w))

        def solve(src):
            dist = [float('inf')]*n
            dist[src] = 0

            h = [[0,src]]

            while h : 
                dis, node = heapq.heappop(h)

                if dis > dist[node]:
                    continue

                for nei, di in adj[node]:
                    new_dis = dis + di
                    if new_dis > distanceThreshold:
                        continue

                    if new_dis < dist[nei]:
                        dist[nei] = new_dis
                        heapq.heappush(h,(new_dis, nei))
            cnt = 0     
            for d in dist:
                if d != 0 and d != float('inf'):
                    cnt+=1
            return cnt, -src              

        new_dist = []
        for i in range(n):
            new_dist.append(solve(i))
        
        heapq.heapify(new_dist)

        cnt, node = new_dist[0]
        return -node

        