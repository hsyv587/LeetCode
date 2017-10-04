# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        p1 = head.next
        head.next = None
        return self.rec_call(head, p1)
    
    def rec_call(self, p_prev, p_curr):
        if not p_curr.next:
            p_curr.next = p_prev
            return p_curr
        p_next = p_curr.next
        p_curr.next = p_prev
        return self.rec_call(p_curr, p_next)
        