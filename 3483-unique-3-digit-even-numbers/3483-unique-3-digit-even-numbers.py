class Solution(object):
    def totalNumbers(self, digits):
        res = set()

        def solve(visited, temp):

            if len(temp) == 3 :
                inti = int("".join(map(str, temp)))
                if inti %2 == 0: 
                    res.add(inti)
                return     
                
            for i in range(len(digits)):
                if not temp and digits[i]==0:
                    continue
                    
                if i not in visited:
                    visited.add(i)
                    temp.append(digits[i])

                    solve(visited, temp)

                    temp.pop()
                    visited.remove(i)

        solve(set(),[])
        return len(res)

        