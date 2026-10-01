class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        strnum = str(num)
        rev1 = strnum[::-1]
        intrev1 = int(rev1)
        rev2 = str(intrev1)[::-1]

        return int(rev2) == num
         