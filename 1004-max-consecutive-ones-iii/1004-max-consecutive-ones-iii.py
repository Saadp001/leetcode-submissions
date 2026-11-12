class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, r = 0,0
        n = len(nums)
        maxi = 0

        while r < n:
            if nums[r] == 1:
                r+=1
                maxi = max(maxi, r-l)
            elif nums[r] == 0 and k >0:
                r+=1
                k-=1
                maxi = max(maxi, r-l)
                
            else:
                while nums[l] != 0:
                    l+=1
                l+=1
                k+=1
        return maxi            

















