class Solution:
    def findLucky(self, arr: list[int]) -> int:
        hm = Counter(arr)

        sohm = dict(sorted(hm.items(), reverse = True))

        for key, val in sohm.items():
            if key == val:
                return key

        return -1        