class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums)<2:
            return nums[0]
        nums.sort()
        counter = 0
        while counter<len(nums)-1:
            if nums[counter] != nums[counter+1]:
                return nums[counter]
            counter += 2
        return nums[len(nums)-1]

tests = ([4,1,2,1,2], [1])
for test in tests:
    print(Solution().singleNumber(test))