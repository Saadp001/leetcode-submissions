class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt, no = 0,0
        for num in nums:
            if num < target:
                cnt+=1
            elif num == target:
                no+=1

        return list(range(cnt, cnt + no))    

        
