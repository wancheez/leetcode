class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        jump_len = len(matrix[0]) - 1
        jump_minus = 0
        for inner_start in range(len(matrix[0])):
            for ind in range(0, jump_len - jump_minus):
                left_up = matrix[inner_start][ind + inner_start]
                right_up = matrix[ind+inner_start][jump_len]
                matrix[ind+inner_start][jump_len] = left_up
                right_down = matrix[jump_len][jump_len-ind]
                matrix[jump_len][jump_len-ind] = right_up
                left_down = matrix[jump_len-ind][inner_start]
                matrix[jump_len-ind][inner_start] = right_down
                matrix[inner_start][ind + inner_start] = left_down
            jump_len -= 1
            jump_minus += 1



matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
# matrix = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
# matrix = [[1,2],[3,4]]
for col in range(len(matrix[0])):
    print()
    for row in range(len(matrix[0])):
        print(matrix[col][row], end=',  ')
Solution().rotate(matrix)
print()
print()
for col in range(len(matrix[0])):
    print()
    for row in range(len(matrix[0])):
        print(matrix[col][row], end=',  ')

# [[2,29,20,26,16,28],
#  [12,27,9,25,13,21],
#  [32,33,32,2,28,14],
#  [13,14,32,27,22,26],
#  [33,1,20,7,21,7],
#  [4,24,1,6,32,34]]

# [[4,33,13,32,12,2],
#  [24,1,14,33,27,29],
#  [1,20,32,32,9,20],
#  [6,7,27,2,25,26],
#  [32,21,22,28,13,16],
#  [34,7,26,14,21,28]]