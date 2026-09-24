class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for d in digits:
            s+= str(d)

        s = int(s)+1
        ans = []
        for d in str(s) :
            ans.append(int(d))

        return ans