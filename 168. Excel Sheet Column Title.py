class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        if columnNumber <= 26:
            return chr(ord('A') + columnNumber - 1)

        i = columnNumber // 26
        left = columnNumber - i * 26
        if left == 0:
            left = 26
            i -= 1
        if i >= 0:
            result += self.convertToTitle(i)
        if left > -1:
            result += chr(ord('A') + left -1)
        return result

for i in range(150):
    print(Solution().convertToTitle(i))
