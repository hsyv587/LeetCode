# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        tail = head
        while tail.next:
            tail = tail.next
        self.quickSort(head, tail)
        return head
    
    def quickSort(self, p1, p2):
        if p1 == p2 or p1 == None:
            return 0
        print p1.val, p2.val
        pi_prev, pi = self.partition(p1, p2)
        self.quickSort(p1, pi_prev)
        if pi_prev.next == p2:
            return 0
        self.quickSort(pi.next, p2)
        
        
    def partition(self, p1, p2):
        i, j = p1, p1
        i_prev = p1
        pivot = p2.val
        while j != p2:
            if j.val <= pivot:
                i.val, j.val = j.val, i.val
                i_prev = i
                i = i.next
            j = j.next
        i.val, p2.val = p2.val, i.val
        return i_prev, i