class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l = [0]*(n+1)

        for i in range(n):
            l[nums[i]] = 1
 
        ans = []
        for i in range(1,n+1):
            if l[i] ==0:
                ans.append(i)

        return ans        