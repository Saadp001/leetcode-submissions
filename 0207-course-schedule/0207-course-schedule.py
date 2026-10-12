class Solution:
    def dfs(self, node, visited, path_vi, adj_list):
        visited[node] = 1
        path_vi[node] = 1
        
        for nei in adj_list[node]:
            if visited[nei] == 0:
                x =  self.dfs(nei, visited, path_vi, adj_list)
                if not x:
                    return False
            elif path_vi[nei] == 1:
                return False
        
        path_vi[node] = 0
        return True
        
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        V = numCourses 
        edges = prerequisites

        adj_list = [[] for _ in range(V)]
        
        for u, v in edges:
            adj_list[v].append(u)
        
        visited = [0]*(V+1)
        path_vi = [0]*(V+1)
        
        for i in range(V):
            if visited[i] == 0:
                x =  self.dfs(i, visited, path_vi, adj_list)
                if not x:
                    return False

               
        return True