class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        if head == None:
            return None
        stack = []

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, head

        while fast:
            if len(stack) == k:
                while stack:
                    slow.next = stack.pop()
                    slow = slow.next
            else:
                stack.append(fast)
                fast = fast.next

        if len(stack) == k:
            while stack:
                slow.next = stack.pop()
                slow = slow.next
            slow.next = None
        elif len(stack) > 0:
            slow.next = stack[0]
        else:
            slow.next = None

        return dummy.next

        
def arrToList(arr):
    dummy = ListNode(0)
    cur = dummy

    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next

    return dummy.next

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
    k = 3
    result = sol.reverseKGroup(head, k)
    printList(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(k)')

