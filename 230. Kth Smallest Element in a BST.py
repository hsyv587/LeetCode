# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return null
        result = []
        self.in_order(root, result, k)
        return result[-1]
        
    
    def in_order(self, node, result, k):
        if node.left:
            if self.in_order(node.left, result, k):
                return True
        result.append(node.val)
        if len(result) == k:
            return True
        if node.right:
            if self.in_order(node.right, result, k):
                return True
        return False
        