class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hm = {}
        for i in range(len(knowledge)):
            hm[knowledge[i][0]] = knowledge[i][1]
        
        i = 0
        ans = ""
        while i < len(s):
            k = ""
            if s[i] == "(":
                i+=1            
                while s[i] != ')':
                    k += s[i]
                    i+=1 
                
                if k in hm:
                    ans+= hm[k]    
                else:
                    ans+= '?'
                i+=1
                
            else:    
                ans+= s[i]  
                i+=1     

        return ans    