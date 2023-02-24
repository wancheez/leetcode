class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        left, right, down = 0, len(matrix[0]), len(matrix)
        max_count = right * down
        count = 0
        for _ in range(10):
            if count == max_count:
                return result
            j = left
            while j < right:
                result.append(matrix[left][j])
                j += 1
                count += 1
            if count == max_count:
                return result
            j = left + 1
            while j < down:
                result.append(matrix[j][right-1])
                j += 1
                count += 1
            if count == max_count:
                return result
            j = right - 2
            while j > left:
                result.append(matrix[down-1][j])
                j -= 1
                count += 1
            if count == max_count:
                return result
            j = down - 1
            while j > left:
                result.append(matrix[j][left])
                j -= 1
                count += 1
            if count == max_count:
                return result
            left += 1
            right -= 1
            down -= 1
        return result


tests = ([[3],[2]],
         [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]],
         [
             [1,2,3],
             [4,5,6],
             [7,8,9]],

)
for test in tests:
    print(Solution().spiralOrder(test))