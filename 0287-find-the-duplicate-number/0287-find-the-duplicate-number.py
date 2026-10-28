class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

            if hm[num] >1:
                return num         