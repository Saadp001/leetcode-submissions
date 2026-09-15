class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            maxi = 0
            for c in str(num):
                maxi = max(maxi,int(c))
            new = ""
            for _ in range(len(str(num))):
                new += str(maxi)

            total+= int(new)
 
        return total        

