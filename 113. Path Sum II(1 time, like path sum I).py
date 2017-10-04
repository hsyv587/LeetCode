# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.rec(root, [], 0, sum, res)
        return res
    def rec(self, node, curr, curr_sum, sum, res):
        if not node.left and not node.right and curr_sum + node.val == sum:
            res.append(curr + [node.val])
            return 0
        if node.left:
            self.rec(node.left, curr + [node.val], curr_sum + node.val, sum ,res)
        if node.right:
            self.rec(node.right, curr + [node.val], curr_sum + node.val, sum, res)