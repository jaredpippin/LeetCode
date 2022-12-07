# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o_head = ListNode(0)
        o = o_head

        e_head = ListNode(0)
        e = e_head
        i = 0
        while (head != None):
            if (i % 2 == 0):
                o.next = head
                o = head
            else:
                e.next = head
                e = head
            head = head.next
            i += 1
        e.next = None
        o.next = e_head.next

        return o_head.next

