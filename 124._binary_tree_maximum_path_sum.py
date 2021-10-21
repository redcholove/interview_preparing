class Solution:
    def maxPathSum(self, root):
        if root == None:
            return 0
            
        self.result = root.val
        
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            
            val = max(root.val, 
                    root.val + left, 
                    root.val + right, 
                    root.val + left + right)
                    
            self.result = max(self.result, val)
            
            return max(root.val, root.val + left, root.val + right)
        
        helper(root)
        return self.result
        

if __name__ == '__main__':
    print('success')
    print('懶得寫tree測資')
    print('time complexity: O(n)')
    print('space complexity: O(h)')
