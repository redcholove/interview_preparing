class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
            
        if not p or not q:
            return False
            
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

if __name__ == '__main__':
    print('懶得寫tree的test')
    print('success')
    print('time complexity: O(n) dfs traversal all tree node')
    print('space complexity: O(n)')
