class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #找出三個 由小到大的 nums[i]
        
        first, sec = float('inf'), float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= sec:
                sec = n
            else:
                return True
        
        return False
