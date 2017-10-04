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
        start = root
        while True:
            if not start.left:
                break
            curr = start
            start = curr.left
            while True:
                if curr.left:
                    curr.left.next = curr.right
                    if curr.next:
                        curr.right.next = curr.next.left
                else:
                    break
                if curr.next:
                    curr = curr.next
                else:
                    break
            
        
        
        