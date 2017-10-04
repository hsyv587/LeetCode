# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #iteratively
        if not root:
            return []
        stack1, stack2 = [root], []
        result = []
        reverse = False
        while True:
            result.append([])
            for i in range(len(stack1)):
                result[-1].append(stack1[i].val)
                if stack1[i].left:
                    stack2.append(stack1[i].left)
                if stack1[i].right:
                    stack2.append(stack1[i].right)
            if reverse:
                result[-1].reverse()
            if not stack2:
                break
            stack1, stack2 = stack2, []
            reverse = not reverse
        return result
            
        