class Solution:
    def markedEdgeCell(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == '#' or board[i][j] == 'X':
            return
        
        board[i][j] = '#'
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            self.markedEdgeCell(board, i+dx, j+dy)
        
        
    def calcOutput(self, board):
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def edgeTraversal(self, board):
        m = len(board)
        n = len(board[0])
        startRow, startCol, endRow, endCol = 0, 0, m-1, n-1
        
        for i in range(n):
            if board[startRow][i] == 'O':
                self.markedEdgeCell(board, startRow, i)
        startRow += 1
        
        for i in range(startRow, m):
            if board[i][startCol] == 'O':
                self.markedEdgeCell(board, i, startCol)
        startCol += 1
        
        for i in range(startCol, n):
            if board[endRow][i] == 'O':
                self.markedEdgeCell(board, endRow, i)
        endRow -= 1
        
        for i in range(startRow, endRow+1):
            if board[i][endCol] == 'O':
                self.markedEdgeCell(board, i, endCol)

        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        
        m = len(board)
        n = len(board[0])
        self.edgeTraversal(board)
        self.calcOutput(board)
        
        return board
        
        
