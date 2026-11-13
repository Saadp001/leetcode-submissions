class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res= []
        col = set()
        posdi = set()
        negdi = set()

        board = [['.']*n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy =  [ "".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or (r+c) in posdi or (r-c) in negdi:
                    continue

                col.add(c)
                posdi.add(r+c)
                negdi.add(r-c)
                board[r][c] = 'Q'
                
                backtrack(r+1)

                col.remove(c)
                posdi.remove(r+c)
                negdi.remove(r-c)
                board[r][c] = '.'

        backtrack(0) 
        return res