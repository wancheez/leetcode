class Solution:
    def findMedianSortedArrays_brute_force(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        return self.get_middle(nums)

    def get_middle(self, nums):
        if len(nums) % 2 != 0:
            return nums[len(nums) // 2]
        return ((nums[len(nums) // 2 - 1]) + nums[len(nums) // 2]) / 2

    def findMedianSortedArrays_two_pointers(self, nums1: list[int], nums2: list[int]) -> float:
        if not nums1:
            return self.get_middle(nums2)
        if not nums2:
            return self.get_middle(nums1)
        len_sum = len(nums1) + len(nums2)
        is_odd = len_sum % 2 != 0
        max_ind = len_sum // 2 if not is_odd else len_sum // 2 + 1
        cur_len = 0
        ind1, ind2 = 0, 0
        cur_val = None
        while cur_len < max_ind:
            if ind1<len(nums1) and ind2<len(nums2):
                if nums1[ind1] < nums2[ind2]:
                    cur_val = nums1[ind1]
                    ind1 += 1
                else:
                    cur_val = nums2[ind2]
                    ind2 += 1
            elif ind1 >= len(nums1):
                cur_val = nums2[ind2]
                ind2 += 1
            else:
                cur_val = nums1[ind1]
                ind1 += 1
            cur_len += 1
        if is_odd:
            return cur_val
        if ind1 == len(nums1):
            return (cur_val + nums2[ind2]) / 2
        elif ind2 == len(nums2):
            return (cur_val + nums1[ind1]) / 2
        return (cur_val + min(nums1[ind1], nums2[ind2])) / 2



test = ([1, 3], [2])  # [1,2,3,4,5,6,7]
print(Solution().findMedianSortedArrays_two_pointers(test[0], test[1]))
