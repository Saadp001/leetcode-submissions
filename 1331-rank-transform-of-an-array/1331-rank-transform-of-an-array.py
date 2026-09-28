class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sarr = sorted(arr)
        cnt = 1
        hm = {}
        for num in sarr:
            if num not in hm:
                hm[num] = cnt
                cnt+=1

        res = []
        for num in arr:
            if num in hm:
                res.append(hm[num])

        return res 