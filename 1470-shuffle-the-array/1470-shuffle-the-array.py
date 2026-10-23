class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        x = 0
        y = n
        while x < n:
            ans.append(nums[x])
            x+= 1
            ans.append(nums[y])
            y+=1

        return ans    

