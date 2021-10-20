'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        '''
        1-2-3-4-5
        '''
        if head == None:
            return None
            
        #count len(list) -> make it circular, record new head idx
        
        #traversal from head, tail.next = None, return newHead
        
        hLen = 1
        cur = head
        
        while cur.next:
            hLen += 1
            cur = cur.next
        cur.next = head
        
        idx = hLen - k%hLen
        cur = head
        for i in range(idx-1):
            cur = cur.next
        prev = cur.next
        cur.next = None
        
        return prev
    
def arrToList(arr):
    result = ListNode(0)
    cur = result
    
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return result.next
    
def printList(head):
    cur = head
    arr = []
    while cur:
        arr.append(cur.val)
        cur = cur.next
    print(arr)

if __name__ == '__main__':
    sol = Solution()
    head = arrToList([0,1,2])
    k = 4
    result = sol.rotateRight(head, k)
    printList(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
