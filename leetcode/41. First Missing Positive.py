class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i
        return len(nums) + 1


tests = ([1], [1,2,0], [3,4,-1,1])
for test in tests:
    print(Solution().firstMissingPositive(test))