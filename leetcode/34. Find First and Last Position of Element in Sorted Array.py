class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start, end = 0, len(nums) - 1
        middle = -1
        found = False
        while end >= start:
            middle = (end + start) // 2
            if nums[middle] == target:
                found = True
                break
            if target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        if not found:
            return [-1, -1]
        right = middle
        left = middle

        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        return [left, right]


tests = (([5,7,7,8,8,10], 6), ([5,7,7,8,8,10], 8), ([], 1))
for nums, target in tests:
    print(Solution().searchRange(nums, target))