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

    def merge2(self, nums1: List[int], len_num1: int, nums2: List[int], len_num2: int) -> None:
        del nums1[len_num1:]
        nums1.extend(nums2)
        nums1.sort()

    def merge(self, nums1: List[int], len_num1: int, nums2: List[int], len_num2: int) -> None:
        a, b, write_ind = len_num1 - 1, len_num2 - 1, len_num1 + len_num2 - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_ind] = nums1[a]
                a -= 1
            else:
                nums1[write_ind] = nums2[b]
                b -= 1
            write_ind -= 1


test_cases = (
    (
        [1, 2, 3, 0, 0, 0], [2, 5, 6]
    ),
)
for nums1, nums2 in test_cases:
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
