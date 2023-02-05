class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{:032b}".format(n)[::-1], 2)

print(Solution().reverseBits(43261596))