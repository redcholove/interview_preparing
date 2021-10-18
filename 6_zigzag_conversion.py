'''

"PAYPALISHIRING"
P   A   H   N
A P L S I I G
Y   I   R
"PAHNAPLSIIGYIR"
'''

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
            
        orderList = [[] for _ in range(numRows)]
        idx = 0
        step = 1
        result = ''
        
        for i in s:
            orderList[idx].append(i)
            idx += step
            
            if idx == 0:
                step = 1
            if idx == numRows - 1:
                step = -1
                
        for i in range(len(orderList)):
            for j in range(len(orderList[i])):
                result += orderList[i][j]
                
        return result

if __name__ == '__main__':
    sol = Solution()
    s = 'PAYPALISHIRING'
    numRows = 3
    result = sol.convert(s, numRows)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
    
