class Solution(object):
    def isPalindrome(self, x):
        xs = str(x)

        l = 0
        r = len(xs) -1

        while l < r:
            if xs[l] != xs[r]:
                return False
            l+=1
            r-=1    

        return True        


