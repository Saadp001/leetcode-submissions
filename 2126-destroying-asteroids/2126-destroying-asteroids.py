class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        nums = asteroids
        nums.sort()

        for a in nums:
            if mass >= a:
                mass+=a

            else:
                return False

        return mass > 0            