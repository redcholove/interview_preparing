# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        lastSorted = head
        cur = head.next
        
        while cur:
            if cur.val >= lastSorted.val:
                lastSorted = cur
                cur = cur.next
            else:
                prev = dummy
                
                while prev.next.val <= cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                next = prev.next
                prev.next = cur
                prev.next.next = next
                cur = lastSorted.next
        return dummy.next
        
                
                
                
