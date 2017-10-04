# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.maxDepth(root) == -1:
            return False
        return True
    def maxDepth(self, curr):
        max_left, max_right = 0, 0
        if curr.left:
            max_left = self.maxDepth(curr.left)
            if max_left == -1:
                return -1
        if curr.right:
            max_right = self.maxDepth(curr.right)
            if max_right == -1:
                return -1
        if abs(max_left - max_right) > 1:
            return -1
        return max(max_left, max_right) + 1
        