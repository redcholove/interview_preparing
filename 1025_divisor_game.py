class Solution:
    def divisorGame(self, n):
        #alice, bob 輪流玩遊戲
        #alice 先
        
        #黑板上面有一個number n
        #每個玩家輪流到的時候可以做
        
        #選擇任意一個 x, 0<x<n and n % x == 0
        #replacing n = n - x
        
        #如果玩家沒辦法做move -> lose
        
        #return true -> 如果只有alice可以贏那場比賽
        
        #假設雙方都很會玩
        
        #可以選擇一個數字 在0跟n之間 而且可以整除n 
        #讓n-x為新的value
        
        
        #lose -> 找不到 0~n 之間 可以被n整除的數字
        
        #除了 0 跟 1之外 基本上都找得到
        
        '''
        n = 多少的時候 當前玩家狀態
        0 -> L
        1 -> L
        2 -> W
        3 -> L
        4 -> W
        '''
        
        #dp -> dp[i] = 當前玩家的 勝負狀態
        #dp[n] = dp[1~n-1] (%n == 0) or True False -> 只要有一個是true 就是true
        #return dp[n]
        
        dp = [False for _ in range(n+1)]
        for i in range(2, n+1):
            #i = 2
            #j = 1
            for j in range(1, i):
                if i % j == 0:
                    curVal = False if dp[i-j] else True
                    dp[i] = (curVal or dp[i])
                    
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    n = 100
    result = sol.divisorGame(n)
    print(result)
    print('success')
    print('time complexity: O(n^2)')
    print('space complexity: O(n)')
