from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        horizontals = defaultdict(set)  # key - номер строки, value - уникальные значения
        verticals = defaultdict(set)  # key - номер колонки, value - уникальные значения колонки
        blocks = defaultdict(set)  # key - номер квадрата, value - уникальные значения квадрата

        for col in range(9):
            for row in range(9):
                val = board[col][row]
                if val != ".":
                    try:
                        self.append_unique(val, horizontals[row])
                        self.append_unique(val, verticals[col])
                        self.append_unique(val, blocks[(row // 3, col // 3)])
                    except ValueError:
                        return False
        return True

    def append_unique(self, value: str, unique_set: set):
        if value in unique_set:
            raise ValueError
        unique_set.add(value)


var = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(var))