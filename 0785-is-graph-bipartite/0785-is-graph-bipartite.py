class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph) 
    
        color = [0]*n
        for i in range(n):
            if color[i] ==0:
                color[i] = 1
                q = deque([i])

                while q:
                    len_q = len(q)
                    
                    for _ in range(len_q):
                        node = q.popleft()

                        for nei in graph[node]:
                            if color[nei] == 0:
                                color[nei] = 3 - color[node] 
                                q.append(nei)

                            if color[nei] == color[node]:
                                return False

        return True                    



