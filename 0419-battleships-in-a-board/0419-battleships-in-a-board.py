class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        grid = board
        m = len(grid)
        n = len(grid[0])
        directions = {(1,0),(-1,0),(0,-1),(0,1)}
        visit = set()
        ans = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 

            if grid[i][j] == '.':
                return 

            if (i,j) in visit:
                return

            visit.add((i,j))

            for di, dj in directions:
                dfs(i+di, j+dj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X' and (i,j) not in visit:
                    ans+=1
                    dfs(i,j)

        return ans                               
