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
        new_head = None
        t_head = ListNode(head.val - 1)
        t_head.next = head
        p_prev = t_head
        p = head
        pn = None
        while p:
            if p.next and p.val != p.next.val and p.val != p_prev.val:
                if not new_head:
                    new_head = p
                    pn = new_head
                else:
                    pn.next = p
                    pn = pn.next
            elif not p.next:
                if p.val != p_prev.val:
                    if not new_head:
                        new_head = p
                    else:
                        pn.next = p
                        pn = pn.next
            p = p.next
            p_prev = p_prev.next
        if pn:
            pn.next = None
        return new_head
            
        