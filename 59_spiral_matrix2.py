'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
'''

class Solution:
    def generateMatrix(self, n):
        #core concept -> n >= 1
        result = [[0 for _ in range(n)] for _ in range(n)]
        val = 1
        startRow, startCol, endRow, endCol = 0, 0, n, n
        
        while val <= n*n:
            for i in range(startCol, endCol):
                result[startRow][i] = val
                val += 1
            startRow += 1
            
            for i in range(startRow, endRow):
                result[i][endCol-1] = val
                val += 1
            endCol -= 1
            
            for i in range(endCol-1, startCol-1, -1):
                result[endRow-1][i] = val
                val += 1
            endRow -= 1
            
            for i in range(endRow-1, startRow-1, -1):
                result[i][startCol] = val
                val += 1
            startCol += 1
        return result
        
        
if __name__ == '__main__':
    sol = Solution()
    n = 3
    result = sol.generateMatrix(n)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
