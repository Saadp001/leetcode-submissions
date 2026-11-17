
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        arr = [text.split(",") for text in transactions]
        res = set()

        for i in range(len(arr)):
            if int(arr[i][2]) > 1000:
                res.add(i)

            for j in range(i + 1, len(arr)):
                if arr[i][0] == arr[j][0]:
                    if arr[i][3] != arr[j][3]:
                        if abs(int(arr[i][1]) - int(arr[j][1])) <= 60:
                            res.add(i)
                            res.add(j)

        return [transactions[i] for i in res]
