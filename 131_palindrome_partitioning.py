class Solution:
    def isPal(self, s1):
        return s1 == s1[::-1]
    
    def dfs(self, s, path, result):
        #s = empty -> result.append(path) return
        if len(s) == 0:
            result.append(path)
            return
        
        r = 0
        
        while r < len(s):
            subString = s[:r+1]
            
            if self.isPal(subString):
                self.dfs(s[r+1:], path + [subString], result)
            r += 1
        return
    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        sLen = len(s)
        
        if sLen == 0:
            return result
        
        #找出所有 substring皆為palindrome的組合
        
        self.dfs(s, [], result)
        
        return result
