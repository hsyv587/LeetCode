# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) / 2
        root = TreeNode(None)
        self.recConstruct(nums, root, 0, len(nums) - 1)
        return root
    
    def recConstruct(self, nums, parent, left, right):
        mid = left + (right - left) / 2
        parent.val = nums[mid]
        if mid - left != 0:          
            parent.left = TreeNode(None)
            self.recConstruct(nums, parent.left, left, mid - 1)
        if right - mid != 0:
            parent.right = TreeNode(None)
            self.recConstruct(nums, parent.right, mid + 1, right)