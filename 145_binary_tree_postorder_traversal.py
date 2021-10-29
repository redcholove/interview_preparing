# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left, right, root
        result = []
        
        def recursive(root):
            if not root:
                return
            
            recursive(root.left)
            recursive(root.right)
            result.append(root.val)
        
        recursive(root)
        return result
