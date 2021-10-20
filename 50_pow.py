'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
'''

class Solution:
    def myPow(self, x, n):
        #求x的n次方

        #2^2 = 2^1 * 2^1
        #2^4 = 2^2 * 2^2
        #2^5 = 2^2 * 2^2 * 2

        #2^-2 = 1/2^1 / 2^1
        
        #kinda of binary search
        if n == 0:
            return 1.0

        half = self.myPow(x,int(n/2))

        if n % 2 == 0:
            return half * half

        if n > 0:
            return half * half * x
        else:
            return half * half / x


if __name__ == '__main__':
    sol = Solution()
    x = 2.0
    n = 10
    result = sol.myPow(x, n)
    print(result)
    print('success')
    print('time complexity: O(log n)')
    print('space complexty: O(n)')
