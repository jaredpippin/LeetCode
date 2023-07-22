# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head #set our slow and fast pointers to beginning of list
        
        while fast and fast.next: #check if null
            
            slow = slow.next #slow pointer
            fast = fast.next.next #fast pointer
            
            if slow == fast: #when the two pointers meet, there is a cycle
                return True
            
        return False #else return False, no cycle if there is a null node reached