class Solution:
    def uniquePaths(self, m, n):
        #一個m*n矩陣
        #從左上到右下有幾種unique path
        
        if m == 0 or n == 0:
            return 0
            
        #dp[i][j] = i,j格的unique path
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    m = 3
    n = 7
    result = sol.uniquePaths(m, n)
    print(result)
    print('success')
    print('time complexity: O(m*n)')
    print('space complexity: O(m*n)')
