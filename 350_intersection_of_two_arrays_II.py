class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #hash map 
        counter = collections.Counter()
        result = []
        
        for n in nums1:
            counter[n] += 1
        
        for n in nums2:
            counter[n] -= 1
            
            if counter[n] >= 0:
                result.append(n)
                
        return result
