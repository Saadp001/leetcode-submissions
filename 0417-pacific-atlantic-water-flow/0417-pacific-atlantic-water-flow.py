class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        pacific = set()
        atlantic = set()

        def dfs(i, j, visit):
            visit.add((i, j))

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if (0 <= ni < m and 0 <= nj < n
                    and (ni, nj) not in visit
                    and heights[ni][nj] >= heights[i][j]):

                    dfs(ni, nj, visit)

        # Pacific: top and left borders
        for j in range(n):
            dfs(0, j, pacific)
        for i in range(m):
            dfs(i, 0, pacific)

        # Atlantic: bottom and right borders
        for j in range(n):
            dfs(m - 1, j, atlantic)
        for i in range(m):
            dfs(i, n - 1, atlantic)

        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])

        return ans