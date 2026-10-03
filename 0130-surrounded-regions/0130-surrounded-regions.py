class Solution:
    def solve(self, board: list[list[str]]) -> None:

        m = len(board)
        n = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        def dfs(i, j, component):

            # We reached outside the board
            # → this component is connected to the border
            if i < 0 or i >= m or j < 0 or j >= n:
                return True

            # Stop at X or already visited cell
            if board[i][j] == 'X' or (i, j) in visit:
                return False

            visit.add((i, j))
            component.append((i, j))

            connected_to_border = False

            # Explore all 4 directions
            for di, dj in directions:
                if dfs(i + di, j + dj, component):
                    connected_to_border = True

            return connected_to_border

        for i in range(m):
            for j in range(n):

                if board[i][j] == 'O' and (i, j) not in visit:

                    # Store all cells belonging to this island/region
                    component = []

                    connected = dfs(i, j, component)

                    # If it DOES NOT touch border → flip entire component
                    if not connected:
                        for x, y in component:
                            board[x][y] = 'X'