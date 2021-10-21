'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

class Solution:
    def palChecker(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def isPalindrome(self, s):
        tmpString = ''
        for i in s:
            if i.isalpha() or i.isnumeric():
                tmpString += i.lower()
        return self.palChecker(tmpString)
        #trim
        #to lowercase
        #check palindrome
        

if __name__ == '__main__':
    sol = Solution()
    s = "0P"
    result = sol.isPalindrome(s)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
