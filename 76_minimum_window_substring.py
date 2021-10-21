import collections
'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
    def minWindow(self, s, t):
        #找出s裡面 包含t所有字母的 最短length substring
        #slide window + two pointer
        
        #l, r, windowSize, matchSize, matchCounter, tCounter, len(s), len(t), len(result), result
        
        #先move r -> count windowSize, matchSize, matchCounter
        #matchSize == len(t) -> 開始l往右移 然後計算 size
        sLen, tLen, rLen = len(s), len(t), len(s) + 1
        result = ''
        windowSize, matchSize = 0, 0
        l, r = 0, 0
        matchCounter, tCounter = collections.Counter(), collections.Counter()
        if sLen < tLen:
            return result
        
        for i in t:
            tCounter[i] += 1
        
        while r < sLen:
            if s[r] in tCounter:
                matchCounter[s[r]] += 1
                
                if matchCounter[s[r]] <= tCounter[s[r]]:
                    matchSize += 1
            windowSize += 1
            r += 1
            
            while matchSize == tLen:
                if windowSize < rLen:
                    result = s[l:r]
                    rLen = windowSize
                    
                if s[l] in tCounter:
                    matchCounter[s[l]] -= 1
                    
                    if matchCounter[s[l]] >= 0 and matchCounter[s[l]] < tCounter[s[l]]:
                        matchSize -= 1
                windowSize -= 1
                l += 1
        return result
                        
            
        
        
    
if __name__ == '__main__':
    sol = Solution()
    s = "cabwefgewcwaefgcf"
    t = "cae"
    result = sol.minWindow(s, t)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
