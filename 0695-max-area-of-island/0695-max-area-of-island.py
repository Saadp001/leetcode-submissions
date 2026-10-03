class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = {(1,0),(-1,0),(0,-1),(0,1)}
        visit = set()
        ans = 0
        
        maxi = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0

            if grid[i][j] == 0:
                return 0

            if (i,j) in visit:
                return 0

            visit.add((i,j))
            area = 1

            for di, dj in directions:
                area += dfs(i+di, j+dj)
  
            return area       
      
        for i in range(m):
            for j in range(n):      
                if grid[i][j] == 1 and (i,j) not in visit:                   
                    area = dfs(i,j)
                    maxi = max(maxi,area)    
  
        return maxi                             
