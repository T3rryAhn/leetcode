class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()

        # 기울기
        a = 0

        count = 1
        if len(stockPrices) > 1:
            a = (stockPrices[1][1] - stockPrices[0][1]) / (stockPrices[1][0] - stockPrices[0][0])

        for i in range(2, len(stockPrices)):
            n_a = (stockPrices[i][1] - stockPrices[i - 1][1]) / (stockPrices[i][0] - stockPrices[i - 1][0])
            if a == n_a:
                a = n_a
                continue
            else:
                count += 1
                a = n_a

        return count