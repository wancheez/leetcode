from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(2, numRows+1):
            result.append([])
            for j in range(1, i+1):
                if j == 1 or j == i:
                    result[i-1].append(1)
                else:
                    result[i-1].append(result[i-2][j-2] + result[i-2][j-1])
        return result

print(Solution().generate(numRows=5))