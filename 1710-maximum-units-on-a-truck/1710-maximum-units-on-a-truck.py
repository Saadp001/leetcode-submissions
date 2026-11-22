class Solution:
    def maximumUnits(self, boxTypes, truckSize):

        truck_capacity = truckSize
        max_units = 0

        boxTypes.sort(key=lambda x: x[1])

        for i in range(len(boxTypes) - 1, -1, -1):

            if boxTypes[i][0] <= truck_capacity:
                curr_units = boxTypes[i][0] * boxTypes[i][1]
                max_units += curr_units
                truck_capacity -= boxTypes[i][0]

            else:
                curr_units = boxTypes[i][1] * truck_capacity
                max_units += curr_units
                break

        return max_units