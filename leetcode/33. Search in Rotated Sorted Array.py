class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.search_relative(nums, target, 0, len(nums) - 1)

    def search_relative(self, nums: list[int], target: int, start: int, end: int) -> int:
        middle = start + (end - start) // 2
        if nums[middle] == target:
            return middle
        if start == end:
            return -1
        if nums[start] < nums[middle]:  # без ротации слева
            if nums[start] <= target < nums[middle]:  # есть ли там искомое?
                return self.search_relative(nums, target, start, middle - 1)  # left
        if nums[start] > nums[middle]:  # с ротацией слева
            if (nums[start] == target) \
                    or (nums[start] > target and target < nums[middle]) \
                    or (nums[start] < target and target > nums[middle]):
                return self.search_relative(nums, target, start, middle - 1) # left
        # если ничего не подошло слева, то в любом случае идем направо
        return self.search_relative(nums, target, middle + 1, end)  # right

    def search_wo_recursive(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

    def search_linear(self, nums: list[int], target: int):
        for i in range(0, len(nums) -1):
            if nums[i] == target:
                return i
        return -1



tests = (([8,9,2,3,4], 9), ([5,1,3], 5), ([4,5,6,7,0,1,2], 0), ([5,1,3], 3),   ([3,1], 1), ([1,3], 1), ([1], 0), ([4,5,6,7,0,1,2], 3), ([0,1,2,3,4,5,6,7],6),  )
for nums, target in tests:
    print(Solution().search(nums, target))