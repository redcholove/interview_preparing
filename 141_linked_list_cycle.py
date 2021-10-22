class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        #簡單說就是判斷linked list有沒有cycle
        #floyed's algorithm
        #fast, slow pointer

        if not head:
            return False

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

def buildCycleList():
    head = ListNode(0)
    cur = head
    cur.next = ListNode(1)
    cur = cur.next
    cur.next = ListNode(2)
    cur = cur.next
    cur.next = head
    return head

if __name__ == '__main__':
    sol = Solution()
    head = buildCycleList()
    result = sol.hasCycle(head)
    print(result)
    print('succes')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
