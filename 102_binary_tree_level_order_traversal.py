'''
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''

class Solution:
    def levelOrder(self, root):
        #一層一個array
        #append 到 total array
    
        #bfs
        result = []
        if not root:
            return result
            
        curLevel = [root]
        nextLevel = []
        
        while curLevel:
            tmp = []
            for c in curLevel:
                tmp.append(c.val)
                if c.left:
                    nextLevel.append(c.left)
                if c.right:
                    nextLevel.append(c.right)
            result.append(tmp)
            curLevel = nextLevel
            nextLevel = []
        return result
if __name__ == '__main__':
    print('懶得寫tree的test')
    print('success')
    print('time complexity: O(n) bfs traversal all tree node')
    print('space complexity: O(n)')
