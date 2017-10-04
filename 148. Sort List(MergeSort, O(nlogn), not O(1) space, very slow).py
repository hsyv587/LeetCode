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
        self.mergeSort(head, tail)
        return head
    
    def mergeSort(self, p1, p2):
    
        if p1 == p2:
            return 0
        temp, mid = p1, p1
        while temp != p2:
            temp = temp.next
            if temp.next:
                temp.next
            else:break
            mid = mid.next
        self.mergeSort(p1, mid)
        self.mergeSort(mid.next, p2)
        self.merge(p1, p2, mid)
    
    def merge(self, p1, p2, mid):
        pm = mid.next
        buff = []
        while True:
            if p1.val <= pm.val:
                buff.append(p1.val)
                p1 = p1.next
                if p1 == mid.next:
                    while pm != p2.next:
                        buff.append(pm.val)
                        pm = pm.next
                    break
            else:
                buff.append(pm.val)
                pm = pm.next
                if pm == p2.next:
                    while p1 != mid.next:
                        buff.append(p1.val)
                        p1 = p1.next
                    break
        
            
                