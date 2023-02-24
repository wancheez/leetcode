import math


class Solution:
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        if -1 < x < 10:
            return True
        x_str = str(x)
        len_str = len(x_str)
        if len_str % 2 != 0:  # odd
            center = len_str // 2
            step = 1
            while step < len_str // 2 + 1:
                if x_str[center - step] != x_str[center + step]:
                    return False
                step += 1
            return True
        else:  # even
            center_right = len_str // 2
            center_left = center_right - 1
            if x_str[center_left] != x_str[center_right]:
                return False
            step = 1
            while step < len_str // 2:
                if x_str[center_left - step] != x_str[center_right + step]:
                    return False
                step += 1
            return True

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if -1 < x < 10:
            return True

        reverted_num = 0
        while x > reverted_num:
            reverted_num = x % 10 + reverted_num * 10
            x //= 10

        return x == reverted_num or x == reverted_num // 10

    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Determine the number of digits in the integer
        num_digits = 0
        temp = x
        while temp > 0:
            num_digits += 1
            temp //= 10

        # Check if the number is a palindrome
        left, right = x, 0
        for i in range(num_digits // 2):
            left, right = left // 10, right * 10 + x % 10
            x //= 10

        # If the number of digits is odd, ignore the middle digit
        if num_digits % 2 != 0:
            x //= 10

        return left == x and right == x
