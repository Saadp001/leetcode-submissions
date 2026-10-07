class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = set()

        def valid(st):
            cnt = 0
            for b in st:
                if b == "(":
                    cnt+=1
                elif b == ')':
                    cnt-=1

                if cnt<0:
                    return False

            return cnt == 0                

        def solve(st, idx):
            if idx == len(s):
                if valid(st):
                    res.add(st)
                return 

            if s[idx].isalpha():
                solve(st+s[idx], idx+1)
            else:    
                solve(st + s[idx], idx+1)
        
                solve(st, idx+1)


        solve("", 0) 
        
        ans = list(res)
        maxi = 0
        for br in ans: 
            cnt = 0
            for i in range(len(br)):         
                if br[i] == '(' or br[i] == ')':
                    cnt+=1
            maxi = max(maxi, cnt)

        
        get = []

        for br in ans:
            cnt = 0
            for i in range(len(br)):
                if br[i] == ')' or br[i] == '(':
                    cnt+=1

            if cnt == maxi:
                get.append(br)

        return get        
