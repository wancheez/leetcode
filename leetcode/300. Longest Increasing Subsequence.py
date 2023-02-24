from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        saved_lengths = {nums[0]: 1}

        for num in nums:
            min_less_len = self.min_less(num, saved_lengths)
            if min_less_len:
                saved_lengths[num] = min_less_len + 1
            else:
                saved_lengths[num] = 1
        return max(saved_lengths.values())

    def min_less(self, val, lengths: dict[int,int]):
        found_less_lengths = set()
        for key in lengths.keys():
            if key < val:
                found_less_lengths.add(key)
        if found_less_lengths:
            max_val = 0
            for key in found_less_lengths:
                max_val = max(max_val, lengths[key])
            return max_val
        else:
            return None



# [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))