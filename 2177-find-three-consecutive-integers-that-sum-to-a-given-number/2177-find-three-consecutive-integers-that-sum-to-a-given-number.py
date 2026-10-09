class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:
            return []

        i = num // 3
        return [i - 1, i, i + 1]