# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        stack = []
        if not root:
            return True
        stack.append([root])
        i = 0
        level = 0
        while True:
            endFlag = True
            stack.append([])
            for i in range(len(stack[level])):
                if not stack[level][i]:
                    continue
                if stack[level][i].left or stack[level][i].right:
                    endFlag = False
                stack[level + 1].append(stack[level][i].left)
                stack[level + 1].append(stack[level][i].right)
            if endFlag:
                return True
            if not self.checkLevel(stack[level + 1]):
                return False
            level += 1
        
    def checkLevel(self, level):
        i, j = 0, len(level) - 1
        while i < j:
            if (level[i] is not None and level[j] is None) or (level[j] is not None and level[i] is None) or (level[i] and level[j] and level[i].val != level[j].val):
                return False
            i += 1
            j -= 1
        return True
        
        
        