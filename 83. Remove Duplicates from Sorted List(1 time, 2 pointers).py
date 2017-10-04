# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = head
        while True:
            if p1 and p1.next:
                p2 = p1.next
            else:return head
            while p2 and p2.val == p1.val:
                p2 = p2.next
            p1.next = p2
            p1 = p2
        