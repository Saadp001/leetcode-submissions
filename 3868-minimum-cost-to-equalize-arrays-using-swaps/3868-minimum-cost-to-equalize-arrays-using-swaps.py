class Solution(object):
    def minCost(self, nums1, nums2):
        h1 = Counter(nums1)
        h2 = Counter(nums2)

        if h1 == h2:
            return 0

        # check if possible
        combined = Counter(nums1 + nums2)
        for val in combined:
            if combined[val] % 2 != 0:
                return -1

        # count cost
        cost = 0
        for val in h1:
            if h1[val] > h2.get(val, 0):
                cost += h1[val] - h2.get(val, 0)
                

        return cost //2