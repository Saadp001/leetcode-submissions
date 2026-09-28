class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sarr = sorted(arr)
        cnt = 1
        hm = {}
        for num in sarr:
            if num not in hm:
                hm[num] = cnt
                cnt+=1

        
        for i in range(len(arr)):
            if arr[i] in hm:
                arr[i] = hm[arr[i]]
 
        return arr