class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    '''
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    n = 2
    1-2-3-4-5
    
    '''
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        
        for i in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
def arrToList(arr):
    result = ListNode(0)
    cur = result
    
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return result.next

def printList(head):
    result = []
    cur = head
    
    while cur:
        result.append(cur.val)
        cur = cur.next
    print(result)

if __name__ == '__main__':
    sol = Solution()
    head = arrToList([1,2,3,4,5])
    n = 2
    result = sol.removeNthFromEnd(head, 2)
    printList(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
