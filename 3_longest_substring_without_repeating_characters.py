class Solution:
    def lengthOfLongestSubstring(self, s):
        appears = dict()
        sLen = len(s)
        result = 0
        start = 0

        for i in range(sLen):
            if s[i] in appears and appears[s[i]] >= start:
                start = appears[s[i]] + 1
            else:
                result = max(i-start+1, result)
            appears[s[i]] = i
        
        return result
        

if __name__ == '__main__':
    sol = Solution()
    inputString = 'abcabcbb'
    result = sol.lengthOfLongestSubstring(inputString)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
