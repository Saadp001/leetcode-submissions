class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def valid(st):
            cnt = 0
            for b in st:
                if b == '(':
                    cnt+=1
                else:
                    cnt-=1

                if cnt<0:
                    return False

            return cnt == 0                

        def solve(st):
            if len(st) == 2*n:
                if valid(st):
                    res.append(st)
                return 

            solve(st+'(')
            solve(st+')')        

        solve("")
        return res       
            
       