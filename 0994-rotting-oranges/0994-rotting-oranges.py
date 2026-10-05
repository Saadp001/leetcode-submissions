from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Put ALL initially rotten oranges into the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        minute = 0

        # Multi-source BFS
        while q:

            # Number of oranges that are rotten at the
            # beginning of this minute
            level_size = len(q)

            for _ in range(level_size):

                i, j = q.popleft()

                # Spread rot to 4 neighbours
                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    # Valid cell + fresh orange
                    if (0 <= ni < m and
                        0 <= nj < n and
                        grid[ni][nj] == 1):

                        grid[ni][nj] = 2
                        q.append((ni, nj))

            # One complete BFS level = one minute
            minute += 1

        # If any fresh orange remains, impossible
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        # If there were no fresh oranges initially,
        # we don't need any minutes.
        return max(0, minute - 1)