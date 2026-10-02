class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        visit = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i >= m or j >= n or i <0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0

            visit.add((i,j))

            perim = dfs(i, j+1)
            perim += dfs(i+1,j)
            perim += dfs(i,j-1)
            perim += dfs(i-1, j)
            return perim

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)            