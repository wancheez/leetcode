class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if -1 < x < 10:
            return True
        x_str = str(x)
        len_str = len(x_str)
        if len_str % 2 != 0:  # odd
            center = len_str//2
            step = 1
            while step < len_str//2+1:
                if x_str[center-step] != x_str[center+step]:
                    return False
                step += 1
            return True
        else:  # even
            center_right = len_str // 2
            center_left = center_right - 1
            if x_str[center_left] != x_str[center_right]:
                return False
            step = 1
            while step < len_str//2:
                if x_str[center_left-step] != x_str[center_right+step]:
                    return False
                step += 1
            return True


tests = [-10, 121,1221, 3221]
for test in tests:
    print(Solution().isPalindrome(test))