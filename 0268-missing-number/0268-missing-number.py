class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # return n * (n + 1) // 2 - sum(nums)

        s = [-1]*(n+1)

        for num in nums:
            s[num] = 1
        print(s)
        for i,num in enumerate(s) : 
            if num == -1:
                return i