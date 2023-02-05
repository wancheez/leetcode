import math


class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        if x == 0:
            return 0
        for i in range(20):
            r = (r + x / r) / 2
        return math.floor(r)


print(Solution().mySqrt(8))
