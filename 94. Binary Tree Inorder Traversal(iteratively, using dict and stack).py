# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        temp_node = root
        parent_stack = []
        result = []
        done = set()
        while True:
            #print temp_node.val
            while temp_node.left and temp_node.left not in done:
                parent_stack.append(temp_node)
                temp_node = temp_node.left
                done.add(temp_node)
            result.append(temp_node.val)
            if temp_node.right:
                temp_node = temp_node.right
                continue
            if len(parent_stack) == 0:
                break
            done.add(temp_node)
            temp_node = parent_stack.pop()
            print result
        return result
        
            