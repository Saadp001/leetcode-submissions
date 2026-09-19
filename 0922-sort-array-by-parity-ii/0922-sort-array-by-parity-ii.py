class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        i = 0 
        for num in nums:
            if num % 2 == 0:
                while i < n:
                    ans[i] = num
                    i+=2
                    break

        j = 1 
        for num in nums:
            if num % 2 != 0:
                while j < n:
                    ans[j] = num
                    j+=2
                    break        

        return ans    

            