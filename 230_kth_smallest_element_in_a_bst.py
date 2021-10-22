class Solution:
    def kthSmallest(self, root, k):
        #給一個binary search tree
        #return 第k小的value


        #core concept 他是一顆binary search tree

        #直覺1 -> inorder traversal -> asc sorted order

        #dfs + inorder traversal

        #keep array 直到第k個數字出現
        arr = []
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            arr.append(root.val)
            root = root.right
            if len(arr) == k:
                return arr[-1]




if __name__ == '__main__':
    print('success')
    print('懶得寫樹的測試')
    print('time complexity: O(k)')
    print('space complexity: O(k)')
