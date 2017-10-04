# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.rec(root, 0, sum)
        
    def rec(self, node, sum_curr, sum):
        if not node.left and not node.right and sum_curr + node.val == sum:
            return True
        if node.left:
            if self.rec(node.left, sum_curr + node.val, sum):
                return True
        if node.right:
            if self.rec(node.right, sum_curr + node.val, sum):
                return True
        return False