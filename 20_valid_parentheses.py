class Solution:
    def isValid(self, inputString):
        mapping = { ')': '(', '}': '{', ']': '['}
        stack = []
        
        for s in inputString:
            if s in mapping:
                if not stack:
                    return False
                else:
                    if stack.pop() != mapping[s]:
                        return False
            else:
                stack.append(s)
        if stack:
            return False
            
        return True

if __name__ == '__main__':
    inputString = '()[]{}'
    sol = Solution()
    result = sol.isValid(inputString)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
