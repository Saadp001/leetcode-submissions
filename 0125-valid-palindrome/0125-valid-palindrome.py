class Solution:
    def isPalindrome(self, s: str) -> bool:
        st =""
        for char in s:
            if char.isalnum():
                st+=char.lower()

        l = 0
        r = len(st)-1
        while l <=r:
            if st[l] != st[r]:
                return  False
            else:
                l+=1
                r-=1
 
        return True                  