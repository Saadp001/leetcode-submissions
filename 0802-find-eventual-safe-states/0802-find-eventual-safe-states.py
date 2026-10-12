class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        outdegree = [0]*n

        adj = [[] for _ in range(n)]

        for node in range(n):
            outdegree[node] = len(graph[node])

            for nei in graph[node]:
                adj[nei].append(node)
 
        q = deque()

        for i in range(n):
            if outdegree[i] ==0:
                q.append(i)

        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in adj[node]:
                outdegree[nei] -= 1

                if outdegree[nei] == 0:
                    q.append(nei)

        return sorted(ans)            

