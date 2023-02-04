# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        array_center = len(nums) // 2
        root = TreeNode(
            nums[array_center],
            self.sortedArrayToBST(nums[:array_center]),
            self.sortedArrayToBST(nums[array_center+1:]),
        )
        return root
