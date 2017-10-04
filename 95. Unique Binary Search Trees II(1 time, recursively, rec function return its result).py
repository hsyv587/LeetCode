# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        remain = [i + 1 for i in range(n)]
        return self.Construct(remain[:])
    
    def Construct(self, remain):
        if len(remain) == 1:
            return [TreeNode(remain[0])]
        if not remain:
            return [None]
        t_res = []
        for i in range(len(remain)):
            leftTrees = self.Construct(remain[:i])
            rightTrees = self.Construct(remain[i + 1:])
            for k in leftTrees:
                for l in rightTrees:
                    root = TreeNode(remain[i])
                    root.left = k
                    root.right = l
                    t_res.append(root)
        return t_res
        