from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.left.val



sol = Solution()
sol.checkTree(root=TreeNode(10, TreeNode(val=4), TreeNode(val=6)))
