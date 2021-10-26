# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        slow, fast = head, head
        isCycle = False
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                isCycle = True
                break
                
        if isCycle:
            while head != slow:
                head = head.next
                slow = slow.next
                
            return slow
        else:
            return None
