class Solution:
    number_chars = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> list[str]:
        digits = digits.replace("1", '')
        if not digits:
            return []
        return self.letterCombinations_w_char('', digits)

    def letterCombinations_w_char(self, current_chars: str, digits: str) -> list[str]:
        if not digits:
            return [current_chars]
        result = []
        first_digit = digits[0]
        for char in self.number_chars[first_digit]:
            result += self.letterCombinations_w_char(current_chars + char, digits[1:])
        return result


tests = ("1337", "23", "2", "",)
for test in tests:
    print(Solution().letterCombinations(test))
