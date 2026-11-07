class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm1 = Counter(s)
        hm2 = Counter(t)

        for key, val in hm1.items():
            if key not in hm2:
                return False
            elif val != hm2[key]:
                return False

        return True        
                
