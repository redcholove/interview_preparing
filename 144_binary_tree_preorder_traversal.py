# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def recursive(root):
            if not root:
                return 

            result.append(root.val)
            recursive(root.left)
            recursive(root.right)
        
        def iterator(root):
            if not root:
                return 
            
            stack = [root]
            
            while stack:
                cur = stack.pop()
                result.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        
        iterator(root)
        
        return result
            
