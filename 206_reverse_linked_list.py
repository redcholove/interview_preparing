class Solution:
    def reverseList(self, head):
        if not head:
            return None

        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev

if __name__ == '__main__':
    print('success')
    print('懶得寫測資')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
