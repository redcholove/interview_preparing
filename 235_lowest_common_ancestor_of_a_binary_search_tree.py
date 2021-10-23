class Solution:
    def lowestCommonAncestor(self, root, p, q):
        #重點在於不是 p 或 q
        #就是p跟q的 上一個parent
        
        #dfs
        if root == None: return None
        
        if root == p: return p
        
        if root == q: return q
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and left:
            return root
        else:
            return right or left


if __name__ == '__main__':
    sol = Solution()
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(h)')
