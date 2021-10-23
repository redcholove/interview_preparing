'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s, t):
        #基本上就判斷 字母和出現頻率是否一致
        sLen, tLen = len(s), len(t)
        
        if sLen != tLen:
            return False
            
        counter = collections.Counter()
        for i in s:
            counter[i] += 1
        
        for i in t:
            if i not in counter:
                return False
            counter[i] -= 1
            if counter[i] < 0:
                return False
        return True
        
if __name__ == '__main__':
    so = Solution()
    s = 'anagram'
    t = 'nagaram'
    result = sol.isAnagram(s, t)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
            
