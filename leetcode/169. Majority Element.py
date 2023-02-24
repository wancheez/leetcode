from collections import defaultdict


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_count = len(nums) // 2
        nums.sort()
        cur = nums[0]
        prev = cur
        cur_count = 1
        for num in nums[1:]:
            if num == prev:
                cur_count += 1
                if cur_count > majority_count:
                    return num
            else:
                cur_count = 1
                prev = num
        return cur

print(Solution().majorityElement([1]))