# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        p_curr = head
        p_left_previous = None
        for i in range(n):
            if i == m - 2:
                p_left_previous = p_curr
            elif i == m - 1:
                p_left = p_curr
                p_prev = p_curr
            elif i >= m and i < n:
                p_next = p_curr.next
                p_curr.next = p_prev
                p_prev = p_curr
                p_curr = p_next
                continue
            p_curr = p_curr.next
        if p_left_previous:
            p_left_previous.next = p_prev
            p_left.next = p_curr
            return head
        else:
            p_left.next = p_curr
            return p_prev