class Solution:
    def invertTree(self, root):
        #反轉二元樹

        if not root:
            return None

        left = root.left
        right = root.right
        
        root.left = right
        root.right = left

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root



if __name__ == '__main__':
    print('success')
    print('懶得寫tree test')
    print('time complexity: O(n)')
    print('space complexity: O(h)')
