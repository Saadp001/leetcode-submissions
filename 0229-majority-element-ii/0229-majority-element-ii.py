class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hm = Counter(nums)
        ans = []
        for key, val in hm.items():
            if val > len(nums)//3:
                ans.append(key)

        return ans        
