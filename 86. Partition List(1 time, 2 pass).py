# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = head
        head1, head2 = None, None
        while p1:
            if not head2 and p1.val >= x:
                head2 = ListNode(p1.val)
            elif not head1 and p1.val < x:
                head1 = ListNode(p1.val)
            p1 = p1.next
        if not head1 or not head2:
            return head
        p = head
        p1, p2 = head1, head2
        first1, first2 = True, True
        while p:
            if p.val >= x:
                if first2:
                    first2 = False
                    p = p.next
                    continue
                p2.next = ListNode(p.val)
                p2 = p2.next
            elif p.val < x:
                if first1:
                    first1 = False
                    p = p.next
                    continue
                p1.next = ListNode(p.val)
                p1 = p1.next
            p = p.next
        p1.next = head2
        return head1
            
            
        