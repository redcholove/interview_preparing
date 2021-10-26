class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #找出最大的 正方形 大小
        
        #dp
        #dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i][j] = 1
        
        
        if not matrix:
            return 0
        
        result = 0
        
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    result = max(result, dp[i][j])
        
        return result * result
