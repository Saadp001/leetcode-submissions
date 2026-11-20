class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm = {}

        for ch in strs:
            key = "".join(sorted(ch)) 

            if key not in hm:
                hm[key] = []

            hm[key].append(ch)

        return list(hm.values())
            
          
