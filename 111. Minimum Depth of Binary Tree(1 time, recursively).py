# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        min_left, min_right = 0, 0
        if root.left:
            min_left = self.minDepth(root.left)
        if root.right:
            min_right = self.minDepth(root.right)
        if min_left == 0 and min_right != 0:
            return min_right + 1
        elif min_left != 0 and min_right == 0:
            return min_left + 1
        return min(min_left, min_right) + 1
        