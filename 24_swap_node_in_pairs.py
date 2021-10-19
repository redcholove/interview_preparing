'''
Input: head = [1,2,3,4]
Output: [2,1,4,3]
d-1-2-3-4


2-1-4-3

d-1-2-3-4-5
        s

2-1-4-3-5

'''


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        #dummy 開始
        #把後面兩個swap
        #指向後面兩個
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy

        while slow.next and slow.next.next:
            first = slow.next
            sec = slow.next.next

            nextRound = sec.next
            first.next = nextRound
            sec.next = first
            slow.next = sec
            slow = slow.next.next

        return dummy.next

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
    sol = Solution()
    head = arrToList([1,2,3,4,5])
    result = sol.swapPairs(head)
    printList(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
