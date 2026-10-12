class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        ind = [0]*numCourses

        for i, j in prerequisites:
            adj[j].append(i)
            ind[i] +=1

        q = deque()

        for i in range(numCourses):
            if ind[i] ==0:
                q.append(i)

        ans = []
        comp = 0
        while q:
            node = q.popleft()
            ans.append(node)
            comp +=1

            for nei in adj[node]:
                ind[nei] -= 1

                if ind[nei] ==0:
                    q.append(nei)
        
        return ans if numCourses == comp else []                 