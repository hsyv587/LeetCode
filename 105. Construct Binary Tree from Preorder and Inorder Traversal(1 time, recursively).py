# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        self.recConstruct(inorder[ : index], preorder[1 : index + 1], root, 'left')
        self.recConstruct(inorder[index + 1 :], preorder[index + 1 : ], root, 'right')
        return root
    
    def recConstruct(self, inorder, preorder, parent, direction):
        if not inorder:
            return 0
        root = TreeNode(preorder[0])
        if direction == 'left':
            parent.left = root
        else:parent.right = root
        index = inorder.index(root.val)
        self.recConstruct(inorder[ : index], preorder[1 : index + 1], root, 'left')
        self.recConstruct(inorder[index + 1 :], preorder[index + 1 : ], root, 'right')
        