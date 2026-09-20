class Solution:
    def processStr(self, s: str) -> str:
        stack = []
 
        for char in s:
            if char ==  '*':
                if stack and stack[-1]:
                    stack.pop()

            elif char == '#':
                stack = stack + stack

            elif char == '%':
                stack = stack[::-1]
            else:
                stack.append(char)

         
   
        return "".join(stack)                                