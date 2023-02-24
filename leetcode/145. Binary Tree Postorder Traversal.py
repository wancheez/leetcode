# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            cur = []
            if root.left:
                cur += self.postorderTraversal(root.left)
            if root.right:
                cur += self.postorderTraversal(root.right)
            cur.append(root.val)
            return cur
        return []