'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times
'''

class Solution:
    def findMin(self, nums):
        #binary search find min number
        #distinct element

        nLen = len(nums)
        if nLen == 1:
            return nums[0]

        l = 0
        r = nLen - 1

        if nums[0] < nums[-1]:
            return nums[0]

        while l < r:
            mid = int(l + (r-l) / 2)
            
            val = nums[mid]
            #一定在某個pivot 被rotated 的 case

            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        '''
        [4,5,6,7,0,1,2]
                 l 
                 r

                 l 
                 r
        '''
        return nums[l]


if __name__ == '__main__':
    sol = Solution()
    nums = [3,4,5,1,2]
    result = sol.findMin(nums)
    print(result)
    print('success')
    print('time complexity: O(log n)')
    print('space complexity: O (1)')
