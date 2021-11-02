# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitList(self, head):
        oddHead, evenHead = head, head.next
        odd, even = oddHead, evenHead
        
        while even and even.next:
            tmp = even.next
            odd.next = tmp
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        
        return oddHead
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #第雙數個node放後面
        #但單數個node放前面
        
        #spilt to two linkedlist (by odd node, even node)
        #connect odd list tail with even list haed
        
        if not head or not head.next:
            return head
        
        result = self.splitList(head)
        
        return result
