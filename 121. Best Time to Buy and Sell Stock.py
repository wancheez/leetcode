from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 10001, -1
        max_delta = 0
        price = -1
        for price in prices:
            if buy > price:
                buy = price
            elif sell < price:
                sell = price
                max_delta = max(max_delta, sell - buy)
                sell = -2
        if price:
            max_delta = max(max_delta, price - buy)
        if sell == -1:
            return 0
        return max_delta


tests = ([5,7,2,7,3,3,5,3,0], [2,1,2,1,0,1,2], [2,4,1],[7,1,5,3,6,4], [7,6,4,3,1])
for test in tests:
    print(Solution().maxProfit(test))