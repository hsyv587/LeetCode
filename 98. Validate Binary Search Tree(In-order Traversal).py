# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        result = []
        return self.pre_order(root, result)
    
    def pre_order(self, node, result):
        if node.left:
            if not self.pre_order(node.left, result):
                return False
        if len(result) and node.val <= result[-1]:
            return False
        result.append(node.val)
        if node.right:
            if not self.pre_order(node.right, result):
                return False
        return True
            
            
            
            
        