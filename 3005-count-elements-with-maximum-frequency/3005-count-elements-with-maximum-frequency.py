class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = Counter(nums)
        
        res = []
        for freq in hm.values():
            res.append(freq)

        cand = max(res)

        return sum(i for i in res if i == cand)    

        
        