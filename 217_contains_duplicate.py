class Solution:
    def containsDuplicate(self, nums):
        nLen = len(nums)
        if nLen <= 1:
            return False
        
        appears = set()
        
        for n in nums:
            if n in appears:
                return True
            else:
                appears.add(n)
        return False
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    result = sol.containsDuplicate(nums)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
