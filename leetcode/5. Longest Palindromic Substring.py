class Solution:
    def longestPalindrome(self, s: str) -> str:

        length_matrix = []
        for i in range(0, len(s)):
            width_matrix = []
            for _ in range(0, len(s)):
                width_matrix.append(0)
            width_matrix[i] = 1
            length_matrix.append(width_matrix)
        if len(s) < 2:
            return s
        for cur_step in range(1, len(s)):
            for ind1 in range(0, len(s) - cur_step):
                ind2 = ind1+cur_step
                if s[ind1] == s[ind2]:
                    between = 0 if ind1 - ind2 <= 1 else length_matrix[ind1 + 1][ind2 - 1]
                    length_matrix[ind1][ind2] = 2 + between
                else:
                    length_matrix[ind1][ind2] = max(
                        length_matrix[ind1][ind2 - 1],
                        length_matrix[ind1+1][ind2],
                    )
        max_value = 0
        max_indexes = (0, 1)
        for ind2 in range(0, len(s) - 1):
            ind1 = len(s) - 1 - ind2
            if length_matrix[ind1][ind2] > max_value:
                max_value = length_matrix[ind1][ind2]
                max_indexes = (ind1, ind2)
        return s[max_indexes[0]: max_indexes[1]+1]


    def is_palindrome(self, s1: str) -> bool:
        return s1 == s1[::-1]

print(Solution().longestPalindrome("ac"))
