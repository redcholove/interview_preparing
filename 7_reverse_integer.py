'''
reversed result in [-2^31, 2^31 - 1]
[2147483647, - 2147483648]

Input: x = 123
Output: 321

Input: x = -123
Output: -321
'''

class Solution:
    def reverse(self, x):
        #123 -> 取3  (3)
        #12 -> 取2   (2)
        #1 -> 取1    (1)
        #x < 0 -> (多-)
        #x > 0 -> return reverse
        
        result = 0
        tmp = abs(x)
        
        while tmp != 0:
            cur = tmp % 10
            result = result * 10 + cur
            tmp = int(tmp / 10)
        if result > 2147483647 or result < -2147483648:
            return 0
        
        if x < 0:
            return result * -1
        else:
            return result


if __name__ == '__main__':
    sol = Solution()
    x = -123
    result = sol.reverse(x)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
