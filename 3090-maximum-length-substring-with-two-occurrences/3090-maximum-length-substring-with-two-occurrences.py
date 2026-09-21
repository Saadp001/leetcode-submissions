class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        r = 0 
        maxi = 1
        while r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1

            while hm[s[r]] > 2:
                hm[s[l]] = hm.get(s[l], 0) -1
                l+=1

            maxi = max(maxi, r-l+1)
            r+=1
        return maxi    


