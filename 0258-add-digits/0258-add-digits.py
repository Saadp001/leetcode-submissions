class Solution:
    def addDigits(self, num: int) -> int:
        
        def solve(num):
            if num < 10:
                return num

            total = 0
            while num:    
                total+= num % 10
                num = num//10
 
            return solve(total)

        return solve(num)    
            
   
