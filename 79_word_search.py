'''
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''

class Solution:
    def exist(self, board, word):
        #找出matrix 裡是否有一條path 組成 word
        #直覺走dfs 因為只要find 一條match path
        
        #traversal board -> compare match word[head], + backtracking
        self.m = len(board)
        self.n = len(board[0])
        self.diretcions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        wLen = len(word)
        if self.m * self.n < wLen:
            return False
        
        def dfs(board, word, i, j):
            if len(word) == 0:
                return True
                
            if i < 0 or i >= self.m or j < 0 or j >= self.n:
                return False
            
            if board[i][j] != word[0]:
                return False
            
            res = False
            tmp = board[i][j]
            board[i][j] = '#'
            for di, dj in self.diretcions:
                res = res or dfs(board, word[1:],i+di, j+dj)
            board[i][j] = tmp
            return res
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if dfs(board, word, i , j):
                        return True
        return False
        

if __name__ == '__main__':
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    result = sol.exist(board, word)
    print(result)
    print('success')
    print('time complexity: O(m*n*4^l)')
    print('space complexity: O(m*n)')
