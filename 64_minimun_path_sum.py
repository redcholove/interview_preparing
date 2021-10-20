class Solution:
    def minPathSum(self, grid):
        #dp[i][j] = 到[i][j]的最小path sum
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
        
    
if __name__ == '__main__':
    sol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    result = sol.minPathSum(grid)
    print(result)
    print('success')
    print('time complexity: O(m*n)')
    print('space complexity: O(m*n)')
