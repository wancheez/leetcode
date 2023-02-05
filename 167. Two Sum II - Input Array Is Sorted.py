from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]


tests = [([2,7,11,15], 9), ([2,3,4], 6)]
for test, target in tests:
    print(Solution().twoSum(test, target))