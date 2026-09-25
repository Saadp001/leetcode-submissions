class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hm = Counter(nums)

        for key, val in hm.items():
            if val >=2:
                return True
        return False        