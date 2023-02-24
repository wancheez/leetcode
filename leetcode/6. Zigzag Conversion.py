class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = []
        for _ in range(numRows):
            rows.append([])
        cur_row = 0
        direction = 'down'
        for char in s:
            rows[cur_row].append(char)
            if cur_row >= numRows -1:
                direction = 'up'
                cur_row -= 1
            elif cur_row == 0:
                cur_row += 1
                direction = 'down'
            elif direction == 'down':
                cur_row += 1
            else:
                cur_row -= 1
        result = ''
        for row in rows:
            result += ''.join(row)
        return result


print(Solution().convert("A", 1))