class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        ans = []

        for num in  nums:
            if num < pivot:
                ans.append(num)

        for num in  nums:
            if num == pivot:
                ans.append(num)        

        for num in  nums:
            if num > pivot:
                ans.append(num)

        return ans