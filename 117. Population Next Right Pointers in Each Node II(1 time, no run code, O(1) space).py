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
            return
        p_curr_level = root
        p_next_level = None
        while p_curr_level:
            while p_curr_level:
                if p_curr_level.left:
                    if not p_next_level:
                        p_next_level = p_curr_level.left
                    if p_curr_level.right:
                        p_curr_level.left.next = p_curr_level.right
                    else:
                        p_t = p_curr_level.next
                        while p_t and not p_t.left and not p_t.right:
                            p_t = p_t.next
                        if p_t:
                            if p_t.left:
                                p_curr_level.left.next = p_t.left
                            elif p_t.right:
                                p_curr_level.left.next = p_t.right
                        #p_curr_level = p_t
                if p_curr_level.right:
                    if not p_next_level:
                        p_next_level = p_curr_level.right
                    p_t = p_curr_level.next
                    while p_t and not p_t.left and not p_t.right:
                        p_t = p_t.next
                    if p_t:
                        if p_t.left:
                            p_curr_level.right.next = p_t.left
                        elif p_t.right:
                            p_curr_level.right.next = p_t.right
                    #p_curr_level = p_t
                p_curr_level = p_curr_level.next
            p_curr_level = p_next_level
            p_next_level = None
            