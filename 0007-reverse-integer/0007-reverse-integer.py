class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        c = str(x)

        MIN = -(2**31)      # -2147483648
        MAX = 2**31 - 1    #  2147483647

        if s[0] == '-':
            l = 1
        else:
            l = 0

        n = len(s)

        rev = "".join(reversed(s[l:n]))
        
        rev = int(rev)

        if rev < -(2**31) or rev > 2**31 - 1:
            return 0

        if c[0] == '-':
            return int('-' + str(rev))
        return rev
