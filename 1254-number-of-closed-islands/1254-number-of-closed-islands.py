
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if grid[i][j] == 1:
                return True

            if (i, j) in visited:
                return True

            visited.add((i, j))

            closed = True

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if not dfs(ni, nj):
                    closed = False

            return closed

        ans = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 0:
                    if dfs(i, j):
                        ans += 1

        return ans
