class Solution:
    def isHappy(self, n: int) -> bool:
        cur = n
        digits = []
        sum = 0
        count = 0
        max_count = 100
        met_vals = set()
        while count<max_count:
            while cur > 0:
                digits.append(cur%10)
                cur //= 10
            if tuple(digits) in met_vals:
                return False
            else:
                met_vals.add(tuple(digits))
            for digit in digits:
                sum += digit*digit
            print(digits, ' sum=', sum)
            if sum == 1:
                return True
            digits = []
            cur = sum
            sum = 0
            count+=1
        return False

print(Solution().isHappy(2))

