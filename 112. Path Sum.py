from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        current_sum = root.val
        if not root.left and not root.right:
            return current_sum == targetSum

        return self.branch_run(root, current_sum, targetSum)

    def has_path_sum_with_sum(self, root: Optional[TreeNode], current_sum: int, targetSum: int) -> bool:
        current_sum = root.val + current_sum
        if not root.left and not root.right:
            return current_sum == targetSum
        return self.branch_run(root, current_sum, targetSum)

    def branch_run(self, root: Optional[TreeNode], current_sum: int, targetSum: int) -> bool:
        if root.left and root.right:
            return (
                    self.has_path_sum_with_sum(root.left, current_sum, targetSum) or
                    self.has_path_sum_with_sum(root.right, current_sum, targetSum)
            )
        if root.left:
            return self.has_path_sum_with_sum(root.left, current_sum, targetSum)
        else:
            return self.has_path_sum_with_sum(root.right, current_sum, targetSum)


test = TreeNode(5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
)
print(Solution().hasPathSum(test, 22))
