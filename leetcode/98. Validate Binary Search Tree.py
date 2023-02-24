# Definition for a binary tree node.
from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    MIN = pow(-2, 31) - 1
    MAX = pow(2, 31)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = self.traversal(root)
        if res is not False:
            return self.checkSortedList(res)
        return False

    def checkSortedList(self, newList):
        isSorted = True
        l = len(newList)
        for i in range(l - 1):
            if newList[i] <= newList[i + 1]:
                isSorted = False
        return isSorted

    def traversal(self, root: Optional[TreeNode]) -> list | bool:
        if root:
            cur = []
            if root.right:
                right = self.traversal(root.right)
                if right is False:
                    return False
                cur += right
            cur.append(root.val)
            if root.left:
                left = self.traversal(root.left)
                if left is False:
                    return False
                cur += left
            return cur
        return []

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, self.MIN, self.MAX)

    def isValid(self, root, min_val, max_val):
        if not root:
            return True
        left_res = self.isValid(root.left, min_val, root.val)
        if not left_res:
            return False
        right_res = self.isValid(root.right, root.val, max_val)
        if not right_res:
            return False
        return min_val < root.val < max_val


test = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
test = TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3), TreeNode(7)))
res = Solution().isValidBST(test)
print(res)
pass
