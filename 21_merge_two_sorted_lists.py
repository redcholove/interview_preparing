'''
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        #l1, l2 為 sorted
        #two pointer -> 取最小的
        result = ListNode(0)
        cur = result
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
        
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        
        return result.next

def arrToList(arr):
    result = ListNode(0)
    cur = result
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return result.next

def printList(head):
    cur = head
    result = []
    while cur:
        result.append(cur.val)
        cur = cur.next
    
    print(result)

if __name__ == '__main__':
    l1 = arrToList([1,2,4])
    l2 = arrToList([1,3,4])
    sol = Solution()
    result = sol.mergeTwoLists(l1, l2)
    printList(result)
    print('success')
    print('time complexity: O(m+n)')
    print('space complexity: O(m+n))
          
