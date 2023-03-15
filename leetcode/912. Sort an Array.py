class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        if length == 1:
            return nums
        sorted_list = self.merge(
            self.sortArray(nums[:length // 2]),
            self.sortArray(nums[length // 2:]),
        )

        return sorted_list

    def merge(self, left_part: list[int], right_part: list[int]):
        left_ind, right_ind = 0, 0
        result_list = []
        while left_ind < len(left_part) or right_ind < len(right_part):
            if left_ind >= len(left_part):
                return result_list + right_part[right_ind:]
            elif right_ind >= len(right_part):
                return result_list + left_part[left_ind:]
            if left_part[left_ind] >= right_part[right_ind]:
                result_list.append(right_part[right_ind])
                right_ind += 1
            else:
                result_list.append(left_part[left_ind])
                left_ind += 1

        return result_list


tests = ([5, 1, 1, 2, 0, 0], [3, 7, 8, 2, 14, 8],)

for test in tests:
    print(Solution().sortArray(test))
