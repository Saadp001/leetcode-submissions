class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s= set()

        for num in nums:
            if num in s:
                return num
            s.add(num)

             
    