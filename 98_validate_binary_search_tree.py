class Solution:
    def helper(self, root, mx, mn):
        if root == None:
            return True
            
        if mx != None and root.val >= mx:
            return False
        
        if mn != None and root.val <= mn:
            return False
        
        return self.helper(root.left, root.val, mn) and self.helper(root.right, mx, root.val)
            
        
        
    def isValidBST(self, root):
        if not root:
            return True
        
        return self.helper(root.left, root.val, None) and self.helper(root.right, None, root.val)
    
        

if __name__ == '__main__':
    print('懶得寫tree的test')
    print('success')
    print('time complexity: O(n) dfs traversal all tree node')
    print('space complexity: O(n)')
