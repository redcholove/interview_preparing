class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
            
        chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = ['']
        
        for d in digits:
            tmp = []
            for c in chars[d]:
                for r in result:
                    tmp.append(r + c)
            result = tmp
        
        return result

if __name__ == '__main__':
    sol = Solution()
    digits = '23'
    result = sol.letterCombinations(digits)
    print(result)
    print('success')
    print('time complexity: O(d*c*r)')
    print('space complexity: O(r)')
