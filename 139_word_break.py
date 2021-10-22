'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s, wordDict):
        sLen = len(s)
        if sLen == 0:
            return True
        
        #dp 
        '''
          l e e t c o d e
       [0,1,2,3,4,5,6,7,8]
       [T,F,F,F,T,F,F,F,T]
        return True
        '''
        dp = [False for _ in range(sLen + 1)]
        dp[0] = True #means empty character

        for i in range(1, sLen + 1):
            if dp[i-1]:
                #i = 1
                for word in wordDict:
                    if len(word) <= sLen + 1 - i and word == s[i-1:i-1+len(word)]:
                        dp[i+len(word)-1] = True
                    
                        if dp[-1] == True:
                            return True
        return False



if __name__ == '__main__':
    sol = Solution()
    s = 'leetcode'
    wordDict = ['leets', 'code']
    result = sol.wordBreak(s, wordDict)
    print(result)
    print('success')
    print('time complexity: O(n * m)')
    print('space complexity: O(n)')
