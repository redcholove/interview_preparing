class Solution:
    def getPrefix(self, str1, str2):
        result = ''
        len1, len2 = len(str1), len(str2)
        index1, index2 = 0, 0
        
        while index1 < len1 and index2 < len2:
            if str1[index1] == str2[index2]:
                result += str1[index1]
                index1 += 1
                index2 += 1
            else:
                break
        return result
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #take pivot 
        #for loop compare every node
        
        if not strs:
            return ''
        
        pivot = strs[0]
        
        for i in range(1, len(strs)):
            #compare string
            pivot = self.getPrefix(pivot, strs[i])
            
            if len(pivot) == 0:
                break
                
        return pivot
