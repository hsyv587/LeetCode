# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.rec(root)
        return root
    
    def rec(self, node):
        node.left, node.right = node.right, node.left
        if node.left:
            self.rec(node.left)
        if node.right:
            self.rec(node.right)
        