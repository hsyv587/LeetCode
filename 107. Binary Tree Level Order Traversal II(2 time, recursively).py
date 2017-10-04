# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [root]
        self.rec(stack, res)
        return res
    
    def rec(self, stack, res):
        t_stack = []
        t_res = []
        for i in stack:
            if i.left:
                t_stack.append(i.left)
            if i.right:
                t_stack.append(i.right)
        if t_stack:
            self.rec(t_stack, res)
        for i in stack:
            t_res.append(i.val)
        res.append(t_res)