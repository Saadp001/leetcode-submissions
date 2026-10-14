class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        V = len(edges)
        adj = [[] for _ in range(V + 1)]

        def dfs(node, target, visited):
            if node == target:
                return True

            visited[node] = 1

            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei, target, visited):
                        return True

            return False

        for i, j in edges:
            visited = [0] * (V + 1)

            if dfs(i, j, visited):
                return [i, j]

            adj[i].append(j)
            adj[j].append(i)

        return []
        