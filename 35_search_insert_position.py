'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
                 l
                 r

l = mid + 1
r = mid
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
                     l     
                     r
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
               l 
               r
Output: 0
Example 5:

Input: nums = [1], target = 0
               l
               r
Output: 0

'''

class Solution:
    def searchInsert(self, nums, target):
        nLen = len(nums)

        if nLen == 0:
            return 0

        l = 0
        r = nLen - 1

        if target > nums[-1]:
            return nLen

        while l < r:
            mid = int(l + (r-l) / 2)
            
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid
            else:
                #nums[mid] < target
                l = mid + 1
        return l


if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,5,6]
    target = 5
    result = sol.searchInsert(nums, target)
    print(result)
    print('success')
    print('time complexity: O(log n)')
    print('space complexity: O(1)')
