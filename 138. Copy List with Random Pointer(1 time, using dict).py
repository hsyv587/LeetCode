# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        visited = {}
        p1 = head
        new_head = RandomListNode(head.label)
        visited[head] = new_head
        while p1:
            if p1 not in visited:
                visited[p1] = RandomListNode(p1.label)
            new_node = visited[p1]
            if p1.random:
                visited[p1.random] = RandomListNode(p1.random.label)
                new_node.random = visited[p1.random]
            if p1.next:
                visited[p1.next] = RandomListNode(p1.next.label)
                new_node.next = visited[p1.next]
            p1 = p1.next
        return new_head