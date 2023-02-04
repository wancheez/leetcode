from typing import List


class Solution:
    def merge1(self, nums1: List[int], len_num1: int, nums2: List[int], len_num2: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        del nums1[len_num1:]
        if not nums1:
            nums1.extend(nums2)
            return
        if not nums2:
            return


        nums1_ind = 0
        for nums2_ind, val in enumerate(nums2):

            if nums1_ind >= len(nums1):
                nums1.extend(nums2[nums2_ind:])
                return
            while val >= nums1[nums1_ind]:
                nums1_ind += 1
                if nums1_ind == len(nums1):
                    nums1.extend(nums2[nums2_ind:])
                    return
            nums1.insert(nums1_ind, val)
            nums1_ind += 1
    def merge(self, nums1: List[int], len_num1: int, nums2: List[int], len_num2: int) -> None:
        del nums1[len_num1:]
        nums1.extend(nums2)
        nums1.sort()




test_cases = (
    (
        [0], [1]
    ),
)
for nums1, nums2 in test_cases:
    Solution().merge(nums1, 0, nums2, 1)
    print(nums1)
