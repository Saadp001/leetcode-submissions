class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        mini = nums[0]
        maxi = nums[len(nums)-1]
        
        seen = set(nums)
        ans = []
        for i in range(mini, maxi+1):
            if i not in seen:
                ans.append(i)

            
        return ans       
      
