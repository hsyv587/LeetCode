# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack, result = [], []
        stack.append(root)
        self.recCheck(stack, result)
        return result
    
    def recCheck(self, stack, result):
        t_stack = []
        result.append([])
        for i in stack:
            result[-1].append(i.val)
            if i.left:
                t_stack.append(i.left)
            if i.right:
                t_stack.append(i.right)
        if not t_stack:
            return 0
        self.recCheck(t_stack, result)
                
            
        
        