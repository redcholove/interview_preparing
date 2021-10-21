'''
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n):
        #走到第三階的 方法 = 第一階的方法 + 第二階的方法
        #explain -> 第一階可以走兩步到第三階, 第二階可以走一步到第三階
        
        #fibnacci
        
        # 1 -> 1, 2 -> 2
        
        if n <= 3:
            return n
        
        dp = [0 for _ in range(n+1)]
        first = 2
        sec = 3
        
        for i in range(4, n+1):
            tmp = first + sec
            first = sec
            sec = tmp
            
        return sec
        
if __name__ == '__main__':
    sol = Solution()
    n = 6
    result = sol.climbStairs(n)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
