# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return root
        stack = [root]
        self.recLevel(stack)
        
    def recLevel(self, stack):
        t_stack = []
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
        
        for i in stack:
            if i.left:
                t_stack.append(i.left)
            if i.right:
                t_stack.append(i.right)
        if not t_stack:
            return 0
        self.recLevel(t_stack)
        
        