# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [0]
        self.rec(root, 0, res)
        return res[0]
    def rec(self, root, prev_sum, res):
        prev_sum = 10 * prev_sum + root.val
        if not root.left and not root.right:
            res[0] += prev_sum
        if root.left:
            self.rec(root.left, prev_sum, res)
        if root.right:
            self.rec(root.right, prev_sum, res)
            
    
    
        