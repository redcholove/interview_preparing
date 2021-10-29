# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left, root, right
        result = []
        def recur(root):
            if not root:
                return 
            
            recur(root.left)
            result.append(root.val)
            recur(root.right)
        
        def iterator(root):
            if not root:
                return 
            
            stack = []
            
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                    
                root = stack.pop()
                result.append(root.val)
                root = root.right
            
        iterator(root)
        return result
            
        return result
