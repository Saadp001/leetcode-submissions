class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:

        n = len(graph)
        visited = [0] * n

        def dfs(node):
            if visited[node] == 1:
                return False

            if visited[node] == 2:
                return True

            visited[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2
            return True

        ans = []

        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans