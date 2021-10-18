class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        #給我兩個linked list
        #把每個node val + 起來
        #return 新的linkedlist
        result = ListNode(0)
        cur = result

        carry = 0
        while l1 != None or l2 != None:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(val)
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(carry)

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
    sol = Solution()
    l1 = arrToList([2,4,3])
    l2 = arrToList([5,6,4])
    result = sol.addTwoNumbers(l1, l2)
    printList(result)
    print('success')
    print('time complexity: O(max(m, n))')
    print('space complexity: O(max(m, n))')
