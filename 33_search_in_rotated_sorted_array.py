'''
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
            
        #binary search
        
        #find mid 
        
        #find asc part
        
        #change l, r
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = int(l + (r-l) / 2)
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[-1]:
                if target > nums[mid] and target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] and target >= nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return - 1
        
if __name__ == '__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = sol.search(nums, target)
    print(result)
    print('success')
    print('time complexity: O(log n)')
    print('space complexity: O(1)')
