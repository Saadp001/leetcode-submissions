class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mini = float("inf")

        ls = landStartTime
        ld = landDuration
        ws = waterStartTime
        wd = waterDuration

        # Land -> Water
        i = 0
        while i < len(ls):
            land_finish = ls[i] + ld[i]

            j = 0
            while j < len(ws):
                water_start = max(land_finish, ws[j])
                finish = water_start + wd[j]

                mini = min(mini, finish)

                j += 1

            i += 1

        # Water -> Land
        k = 0
        while k < len(ws):
            water_finish = ws[k] + wd[k]

            l = 0
            while l < len(ls):
                land_start = max(water_finish, ls[l])
                finish = land_start + ld[l]

                mini = min(mini, finish)

                l += 1

            k += 1

        return mini