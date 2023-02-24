from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        first = 0
        results = []
        while nums[first] <= 0:
            if first > 0 and nums[first-1] == nums[first]:
                if first >= len(nums) - 1:
                    break
                first += 1
                continue
            second = first + 1
            third = len(nums) - 1
            if third < second:
                break
            while third != second and third > second:
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    results.append([nums[first], nums[second], nums[third]])
                if sum <= 0:
                    second += 1
                    if second >= len(nums) - 1:
                        break
                    while nums[second] == nums[second - 1]:
                        second += 1
                        if third == second:
                            break
                else:
                    third -= 1
                    while nums[third] == nums[third + 1] and third > second:
                        third -= 1
                        if third == second:
                            break
            first += 1
        return results




tests = [[-2,0,1,1,2], [0,0,0,0], [0,1,1], [0,0,0], [0,0,0],[-3, 0, 1, 0, 0], [-1,0,1,2,-1,-4], [1,1,-2]]

for test in tests:
    print(Solution().threeSum(test))
