class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict = {}
        for ind, val in enumerate(nums):
            remaining = target - val
            if remaining in my_dict:
                return [ind, my_dict[remaining]]
            my_dict[val] = ind


print(Solution().twoSum([2,7,11,15], 9))