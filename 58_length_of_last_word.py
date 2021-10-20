'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

class Solution:
    def lengthOfLastWord(self, s):
        #回傳整個句子最後一個字的長度
        #一個字的定義為 連續的字母 不包含 space
        
        s = s.split(' ')
        result = 0
        for i in range(len(s)-1, -1, -1):
            tmp = len(s[i])
            if tmp > 0:
                result = tmp
                break
        return result



if __name__ == '__main__':
    sol = Solution()
    s = "luffy is still joyboy"
    result = sol.lengthOfLastWord(s)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('sapce compexity: O(n)')
