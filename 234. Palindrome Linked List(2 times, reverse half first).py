# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        p1, p2 = head, head
        p1_prev = None
        while p2:
            p2 = p2.next
            if p2:
                p2 = p2.next
            p1_prev = p1
            p1 = p1.next
        self.reverse(p1_prev, p1)
        p1, p2 = head, p1_prev.next
        #self.print_list(p1)
        #self.print_list(p2)
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
    def reverse(self, prev, head):
        p_curr = head
        p_prev = None
        while p_curr:
            p_next = p_curr.next
            p_curr.next = p_prev
            p_prev = p_curr
            p_curr = p_next
        prev.next = p_prev
            
    def print_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print res