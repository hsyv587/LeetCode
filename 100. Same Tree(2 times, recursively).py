# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and q and p.val != q.val) or (p and not q) or (q and not p):
            return False
        if p and p.left:
            if q and q.left:
                if not self.isSameTree(p.left, q.left):
                    return False
            else:
                return False
        elif p and not p.left:
            if q.left:
                return False
               
        if p and p.right:
            if q and q.right:
                if not self.isSameTree(p.right, q.right):
                    return False
            else:
                return False
        elif p and not p.right:
            if q.right:
                return False
        return True