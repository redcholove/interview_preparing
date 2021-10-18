class Solution:
    def dfs(self, l, r, path, result):
        if l == 0 and r == 0:
            result.append(path)
            return
        
        if l > r:
            return
        
        if l > 0:
            self.dfs(l-1, r, path+'(', result)
        if r > 0:
            self.dfs(l, r-1, path+')', result)
            
    def generateParenthesis(self, n):
        #dfs
        result = []
        if n == 0:
            return result
            
        self.dfs(n, n, '', result)
        
        return result
        
if __name__ == '__main__':
    sol = Solution()
    n = 3
    result = sol.generateParenthesis(n)
    print(result)
    print('success')
    print('time complexity: O(2^n)')
    print('space complexity: O(?)')
