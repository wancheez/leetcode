class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(''.join(char for char in "{:032b}".format(n) if char == '1'))


print(Solution().hammingWeight(11))
