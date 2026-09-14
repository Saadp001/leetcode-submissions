class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hm = Counter(nums)

        if k == 1:
            ans = -1
            for num in nums:
                if hm[num] == 1:
                    ans = max(ans, num)
            return ans        


        if len(nums) == k:
            return max(nums) 

 
        if hm[nums[0]] == 1 and hm[nums[-1]] == 1:
            if nums[0] > nums[-1]:
                return nums[0]
            else:
                return nums[-1]    

        elif hm[nums[0]] == 1 and hm[nums[-1]] != 1:
            return nums[0]

        elif hm[nums[0]] != 1 and hm[nums[-1]] == 1:  
            return nums[-1]  

        else:
            return -1             