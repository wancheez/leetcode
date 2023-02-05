# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            cur = [root.val]
            if root.left:
                cur += self.preorderTraversal(root.left)
            if root.right:
                cur += self.preorderTraversal(root.right)
            return cur
        return []
