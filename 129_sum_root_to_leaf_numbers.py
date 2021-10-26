class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #dfs
        self.result = 0
        
        def dfs(root, path):
            if not root:
                return
            
            path = path * 10 + root.val
            
            if not root.left and not root.right:
                self.result += path
                return 
            
            if root.left: dfs(root.left, path)
            if root.right: dfs(root.right, path)
            
        dfs(root, 0)
        return self.result       
