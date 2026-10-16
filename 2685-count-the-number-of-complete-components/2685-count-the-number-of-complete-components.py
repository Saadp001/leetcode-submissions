class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node):
            visit[node] = 1
            cnt = 1
            edge = len(adj[node])

            for nei in adj[node]:
                if visit[nei] == 0:
                    c, e = dfs(nei)
                    cnt+= c
                    edge+=e

            return cnt, edge      

        adj = [[] for _ in range(n)]

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = [0]*n
        ans = 0
        for i in range(n):
            if visit[i] == 0:
                cnt, edge =  dfs(i)
                if cnt * (cnt - 1) // 2 == edge//2:
                    ans+=1    

        return ans        