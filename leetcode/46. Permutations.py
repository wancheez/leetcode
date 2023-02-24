class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        result = []
        for ind, num in enumerate(nums):
            nums.pop(ind)
            for variant in self.permute(nums):
                result.append([num] + variant)
            nums.insert(ind, num)
        return result


tests = ([1,2,3, 4], )
for test in tests:
    print(Solution().permute(test))