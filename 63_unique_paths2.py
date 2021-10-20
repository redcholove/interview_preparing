class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        #matrix 從左上到右下
        #1是石頭
        #0是可以走的路
        
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
            
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        

if __name__ == '__main__':
    sol = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    result = sol.uniquePathsWithObstacles(obstacleGrid)
    print(result)
    print('success')
    print('time complexity: O(m*n)')
    print('space compleixty: O(m*n)')
