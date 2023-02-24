class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        multi = 1
        for char in columnTitle[::-1]:
            sum += multi * (ord(char) - ord('A') + 1)
            multi *= 26
        return sum

print(Solution().titleToNumber('A'))