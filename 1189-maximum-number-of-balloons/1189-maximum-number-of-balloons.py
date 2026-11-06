class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
      
        ls = {char:0 for char in "balloon"}
    
        for char in text:
            if char in ls:
                ls[char] = ls.get(char, 0) +1

        mini = float('inf')
        for key, val in ls.items():
            if key == 'l' or key == 'o':
                mini = min(mini, val//2)
            else:
                mini = min(mini, val)

        return mini            
            


            



    
       
