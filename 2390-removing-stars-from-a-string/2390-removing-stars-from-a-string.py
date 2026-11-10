class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == '*':
                stack.pop()
            else:
                stack.append(char)
        st = list(reversed(stack))
        ans = ""

        while st:   
            ans+= st.pop()
          
        return ans          

