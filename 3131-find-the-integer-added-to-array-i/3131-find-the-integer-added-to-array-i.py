class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums2.sort()
        nums1.sort()
        ans = nums2[0] - nums1[0]
        return ans
