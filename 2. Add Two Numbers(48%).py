# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l1_end = False
        l2_end = False
        head = ListNode(0)
        result = head.next = ListNode(0)
        while (not l1_end) or (not l2_end):
            add1 = 0 if l1_end else l1.val
            add2 = 0 if l2_end else l2.val
            sum = (add1 + add2 + carry) % 10
            carry = 1 if (add1 + add2 + carry) >= 10 else 0
            result.val = sum
            if not l1.next:
                l1_end = True
            else:
                l1 = l1.next
            if not l2.next:
                l2_end = True
            else:
                l2 = l2.next
            if (not l1_end) or (not l2_end):
                result.next = ListNode(0)
                result = result.next
            else:
                if carry:
                     result.next = ListNode(1)
        return head.next
            