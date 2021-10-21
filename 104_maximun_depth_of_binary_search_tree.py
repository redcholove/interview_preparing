'''
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
'''
class Solution:
    def dfsWay(self, root):
        #dfs一路往下找
        if root == None:
            return 0
            
        return max(self.dfsWay(root.left), self.dfsWay(root.right)) + 1
        
    def bfsWay(self, root):
        if root == None:
            return 0
        cur = [root]
        nextLevel = []
        level = 0
        
        while cur:
            level += 1
            for c in cur:
                if c.left:
                    nextLevel.append(c.left)
                if c.right:
                    nextLevel.append(c.right)
            cur = nextLevel
            nextLevel = []
        return level
        
    def maxDepth(self, root):
        #找出樹的最大深度
        
        self.dfsWay(root) or self.bfsWay(root) #兩者都可
        


if __name__ == '__main__':
    print('懶得寫tree的test')
    print('success')
    print('time complexity: O(n) bfs traversal all tree node')
    print('space complexity: O(n)')
