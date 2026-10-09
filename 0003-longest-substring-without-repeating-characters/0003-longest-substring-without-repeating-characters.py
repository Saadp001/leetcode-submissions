class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        hs = set()
        l = 0
        r = 0
        maxi = 0
        while r < len(s):  

            while s[r] in hs:
                hs.remove(s[l])
                l+=1       

            if s[r] not in hs:
                hs.add(s[r])
                maxi = max(maxi, r-l+1)                
                r+=1 
 
 
 
        return maxi        