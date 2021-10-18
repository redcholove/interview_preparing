class Solution:
    def hashTagString(self, s):
        result = '#'
        for i in s:
            result += i
            result += '#'
        return result
        
    def findMaxWidthIdx(self, s):
        print(s)
        idx = 0
        maxWidth = -1
        sLen = len(s)
        
        for i in range(sLen):
            curWidth = 0
            l = i-1
            r = i+1
            
            while l >= 0 and r < sLen:
                if s[l] == s[r]:
                    curWidth += 1
                    l -= 1
                    r += 1
                else:
                    break
                
                if curWidth > maxWidth:
                    maxWidth = curWidth
                    idx = i
                    
        return idx, maxWidth
    
    def buildResult(self, s, idx, width):
        start = idx - width
        end = idx + width + 1
        result = ''
        
        for i in range(start, end):
            if s[i] != '#':
                result += s[i]
                
        return result
    
    def longestPalindrome(self, s: str) -> str:
        #manacher's algorithm
        
        #babad -> (#b#a#b#a#d#)
        
        '''
         012345678910
        (#b#a#b#a#d#)
         01030301010
        two pointer
        
        record maxLen, maxLen's idx
        build result
        '''
        
        sLen = len(s)
        
        if sLen <= 1:
            return s
        
        s = self.hashTagString(s)
        idx, width = self.findMaxWidthIdx(s)
        s = self.buildResult(s, idx, width)
        return s

if __name__ == '__main__':
	sol = Solution()
	s = 'babad'
	result = sol.longestPalindrome(s)
	print(result)
	print('success')
	print('time complexity: O(n))
	print('space complexity: O(n))
