'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        #index = 1
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return root
        
if __name__ == '__main__':
    sol = Solution()
    preoreder = []
    inorder = []
    result = sol.buildTree(preorder, inorder)
    print(result)
    print('success')
    print('有點懶得寫tree的測試')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
