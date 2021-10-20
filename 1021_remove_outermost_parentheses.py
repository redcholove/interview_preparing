class Solution:
    def removeOuterParentheses(self, s):
        '''
        "", "(A)", "A+B" -> if A, B are valid
        
        for example "", "()", "(())()", and "(()(()))"
        
        '''
        
        
        #先找出 最大的 valid parentheses
        #l, r
        
        #array -> 每個 當前最大的 valid parenthese component
        
        #for s 
        #l == r insert to arry
        
        #for array
        
        #拔掉 最外層兩個
        result = []
        
        l = 0
        r = 0
        start, end = 0, 0
        sLen = len(s)
        
        for i in range(sLen):
            if s[i] == '(':
                l += 1
            if s[i] == ')':
                r += 1
            
            if l == r:
                end = i
                result.append(s[start:i+1])
                start = i + 1
                l, r = 0, 0
        
        for i in range(len(result)):
            result[i] = result[i][1:-1]
            
        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    s = "(()())(())(()(()))"
    result = sol.removeOuterParentheses(s)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
