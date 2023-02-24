from math import factorial


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 2
        num_1 = 0
        if n % 2 == 1:
            num_1 = 1
        result = 0
        for num_2_current in range(n // 2, -1, -1):
            result += self.combinantions_with_repeats(num_1, num_2_current)
            num_1 += 2
        return result

    def combinantions_with_repeats(self, num_1, num_2):
        return int(factorial(num_1+num_2) / (factorial(num_1) * factorial(num_2)))

    def climbStairs_db(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1, prev2 = 1, 2
        for cur_n in range(3, n + 1):
            prev2 = prev2 + prev1
            prev1 = prev2 - prev1

        return prev2


test_cases = range(4, 10)
for case in test_cases:

    print(f'n={case}, result={Solution().climbStairs(case)}, result_db={Solution().climbStairs_db(case)}')
