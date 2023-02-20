from collections import deque


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = '1'
        for _ in range(n-1):
            prev_dig = result[0]
            cur_count = 1
            new_result = ""
            for char in result[1:]:
                if char == prev_dig:
                    cur_count += 1
                else:
                    new_result += f'{cur_count}{prev_dig}'
                    prev_dig = char
                    cur_count = 1
            new_result += f'{cur_count}{prev_dig}'
            result = new_result
        return result

    def say_to_int(self, n: int):
        if n<10:
            return 10+n
        result = deque()
        divider = pow(10, len(str(int(n) // 10)))
        count_dig = 1
        prev_dig = n // divider
        n %= divider
        divider //= 10

        while n > 0:
            dig = n // divider
            if dig != prev_dig:
                result.append(count_dig)
                result.append(prev_dig)
                count_dig = 1
                prev_dig = dig
            else:
                count_dig += 1
            n %= divider
            divider //= 10
        result_int = 10*count_dig + prev_dig
        mult = 100
        while result:
            result_int += result.pop() * mult
            mult *= 10
        return result_int



tests = (3322251,)

for test in tests:
    print(Solution().countAndSay(4))