class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result_subarrays = []
        current_sum = 0
        #current_subarray = []
        result_count = 0
        current_index = 0
        initial_index = 0
        while current_index < len(nums):

            current_sum += nums[current_index]
            if current_sum == target:
                result_count += 1
                initial_index = current_index
                current_sum = 0
                continue
            if current_index == len(nums) - 1:
                initial_index += 1
                current_index = initial_index
                current_sum = 0
                continue
            current_index += 1

        return result_count


test_arrays = (([1,1,1,1,1], 2), ([-1,3,5,1,4,2,-9], 6))
for test_array in test_arrays[1:]:
    print(Solution().maxNonOverlapping(*test_array))