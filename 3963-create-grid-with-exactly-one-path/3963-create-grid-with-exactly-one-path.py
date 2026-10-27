class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#']*n for _ in range(m)]

        j = 0
        while j<n :
            grid[0][j] = '.'
            j+=1
        i = 0
        while i < m:
            grid[i][n-1] = '.'
            i+=1

        return [''.join(row) for row in grid]      

      