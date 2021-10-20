'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result

        startRow, startCol, endRow, endCol = 0, 0, len(matrix), len(matrix[0])
        #重點是 不一定是正方形, 有可能是長方形

        while startRow < endRow or startCol < endCol:
            if startRow < endRow: #右
                for i in range(startCol, endCol):
                    result.append(matrix[startRow][i])
                startRow += 1
            if startCol < endCol: #下
                for i in range(startRow, endRow):
                    result.append(matrix[i][endCol-1])
                endCol -= 1
            if startRow < endRow:
                for i in range(endCol-1, startCol-1, -1):
                    result.append(matrix[endRow-1][i])
                endRow -= 1
            if startCol < endCol:
                for i in range(endRow-1, startRow-1, -1):
                    result.append(matrix[i][startCol])
                startCol += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = sol.spiralOrder(matrix)
    print(result)
    print('success')
    print('time complexity: O(m*n)')
    print('space complexity: O(m*n)')

