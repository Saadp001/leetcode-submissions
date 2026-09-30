class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()

        h = []
        t = tasks[0][0]  # current time starts at first task's entry
        res = []
        i = 0  # pointer into tasks array

        while i < len(tasks) or h:
            # add all tasks available at current time
            while i < len(tasks) and tasks[i][0] <= t:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))  # (process, idx)
                i += 1

            if h:
                # process one task
                process, idx = heapq.heappop(h)
                t += process
                res.append(idx)
            else:
                # cpu idle, jump to next task's entry time
                t = tasks[i][0]

        return res