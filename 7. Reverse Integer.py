class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)
        if x < 10:
            return x
        result = 0
        multiplier = pow(10, len(str(x))-1)
        while x:
            result += x % 10 * multiplier
            multiplier = multiplier // 10
            x = x // 10
            if result > 2147483647:
                return 0
        return result if not is_negative else result * -1


tests = [123, -123, 120, 1, 1534236469]
for test in tests:
    print(Solution().reverse(test))