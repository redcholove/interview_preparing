class Solution:
    def longestValidParentheses(self, s):
        '''
        ())())()()()())))))
        '''
        result = 0
        l = 0
        r = 0

        for i in s:
            if i == '(':
                l += 1
            if i == ')':
                r += 1
            
            if r == l:
                result = max(r*2, result)
            if r > l:
                r = 0
                l = 0

        l, r = 0, 0

        for i in s[::-1]:
            if i == '(':
                l += 1
            if i == ')':
                r += 1

            if r == l:
                result = max(r*2, result)

            if l > r:
                l = 0
                r = 0
        return result

if __name__ == '__main__':
    sol = Solution()
    s = ')()())'
    result = sol.longestValidParentheses(s)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
