class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = haystack
        n = needle
        i = 0
        while i < len(h):
            if h[i] == n[0]:         
                k = i
                j = 0
                while j < len(n) and k < len(h):
                    if h[k] == n[j]:
                        k+=1
                        j+=1
                    else:
                        break
                if j == len(n):
                    return i        
            i+=1
        return -1
            
 




              