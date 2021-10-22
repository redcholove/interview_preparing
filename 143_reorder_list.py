'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
                 s
                   f
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
                     s
                       f
Output: [1,5,2,4,3]
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def splitList(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        return l1, l2
    
    def printList(self, head):
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)

    def reverseList(self, head):
        prev, cur = None, head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def mergeList(self, l1, l2):
        '''
        1-2-3
        4-5

        1-4-2-5-3
        '''
        head1, head2 = l1, l2

        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp

        return l1

    def reorderList(self, head):
        #頭尾 頭尾 頭尾 這樣merge
        if not head or not head.next:
            return head
        
        l1, l2 = self.splitList(head)
        self.printList(l1)
        self.printList(l2)
        l2 = self.reverseList(l2)
        result = self.mergeList(l1, l2)

        return result
        #split two list by odd, even
        #reverse t2
        #merge t1, t2

def arrToList(arr):
    dummy = ListNode(0)
    cur = dummy
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return dummy.next

def printList(head):
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print(arr)

if __name__ == '__main__':
    sol = Solution()
    head = arrToList([1,2,3,4,5])

    result = sol.reorderList(head)
    printList(result)

