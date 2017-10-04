# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1, p2 = head, None
        i = 0
        while p1:
            p1 = p1.next
            if not p1:
                break
            i += 1
            if p2:
                p2 = p2.next
            if i == n:
                p2 = head
        if p2:
            p2.next = p2.next.next
            return head
        else:
            return head.next