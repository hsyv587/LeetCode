# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p_curr = head
        nums = []
        while p_curr:
            nums.append(p_curr.val)
            p_curr = p_curr.next
        return self.construct(nums[:])
    def construct(self, nums):
        if not nums: 
            return None
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.construct(nums[:mid])
        root.right = self.construct(nums[mid + 1:])
        return root
        