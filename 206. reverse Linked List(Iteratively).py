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
        p_curr = head.next
        head.next = None
        p_prev = head
        while p_curr:
            if not p_curr.next:
                p_curr.next = p_prev
                p_head = p_curr
                break
            p_next = p_curr.next
            p_curr.next = p_prev
            p_prev = p_curr
            p_curr = p_next
        return p_head
            
            
        
        