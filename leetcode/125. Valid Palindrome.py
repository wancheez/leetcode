from collections import defaultdict


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = tuple(val.lower() for val in s if val.isalnum())
        from_begin = 0
        from_end = len(alphanum) - 1
        while from_end != from_begin and from_end > from_begin:
            if alphanum[from_begin] != alphanum[from_end]:
                return False
            from_begin += 1
            from_end -= 1
        return True


s = "race a car"
print(Solution().isPalindrome(s))