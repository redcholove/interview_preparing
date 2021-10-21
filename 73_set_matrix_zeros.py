'''
給定matrix, 把matrix 中0 的上下左右全都改成0
'''

class Solution:
    def setZeroes(self, matrix):
        #試試看能不能O(1)搞定
        
        #set column mapping, row mapping
        
        #traversal matrix, 0 -> update row mapping column mapping
        
        #traversal matrix, update from row mapping column mapping
        
        if not matrix:
            return matrix
        
        m = len(matrix)
        n = len(matrix[0])
        
        rowMapping = [False for _ in range(m)]
        colMapping = [False for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowMapping[i] = True
                    colMapping[j] = True
        
        for i in range(m):
            for j in range(n):
                if rowMapping[i] or colMapping[j]:
                    matrix[i][j] = 0
        

if __name__ == '__main__':
    sol = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix)
    print(matrix)
    print('success')
    print('time complexity: O(m*n)')
    print('space complexity: O(1)')
