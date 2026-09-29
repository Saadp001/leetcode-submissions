class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def solve(num):
            nonlocal seen
            if num == 1:
                return True

            if num in seen:
                return False
            seen.add(num)      
            total = 0 
           
            while num:
                val = num % 10
                total += val*val
                num //= 10

            return solve(total)    
                

        return solve(n)    