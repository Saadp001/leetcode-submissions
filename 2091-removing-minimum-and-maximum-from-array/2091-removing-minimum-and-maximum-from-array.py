class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        mini = float('inf')
        maxi = float('-inf')
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                max_i = i
            if nums[i] < mini:
                mini = nums[i]
                min_i = i
        
        n = len(nums) - 1
        ans = float('inf')

        if max_i < min_i:
            ans = min(min_i - 0 + 1, ans)
            ans = min(n - max_i + 1, ans)
            ans = min((max_i-0+1) + (n-min_i+1), ans)   

        else:
            ans = min(max_i - 0 + 1, ans)
            ans = min(n - min_i + 1, ans)
            ans = min((min_i-0+1) + (n-max_i+1), ans)         

        return ans    
            
                




