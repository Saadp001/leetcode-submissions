class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.strip()

        stack = []
        l, r = 0,0
    
        while r < len(st):
            if st[r] == " ":           
                stack.append(st[l:r])
                while st[r] == " ":
                    r+=1
                l = r
            else:
                r+=1
        stack.append(st[l:r])  
        
        res = ""
        while stack:
            res += stack.pop()
            if stack:
                res+= " "


        return res

