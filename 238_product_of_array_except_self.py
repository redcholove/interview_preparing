'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution:
    def productExceptSelf(self, nums):
        #dp
        
        '''
        [1,2,3,4]
        [24,12,8,6]
        
        [24,24,12,4] right to left
        [1,2,6,24] left to right
        '''
        nLen = len(nums)
        result = [0 for _ in range(nLen)]
        leftProduct = [0 for _ in range(nLen)]
        rightProduct = [0 for _ in range(nLen)]
        
        for i in range(nLen):
            if i == 0:
                leftProduct[i] = nums[i]
            else:
                leftProduct[i] = leftProduct[i-1] * nums[i]
        for i in range(nLen-1, -1, -1):
            if i == nLen - 1:
                rightProduct[i] = nums[i]
            else:
                rightProduct[i] = rightProduct[i+1] * nums[i]
        for i in range(nLen):
            if i == 0:
                result[i] = rightProduct[i+1]
            elif i == nLen-1:
                result[i] = leftProduct[i-1]
            else:
                result[i] = leftProduct[i-1] * rightProduct[i+1]
        return result
        
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4]
    result = sol.productExceptSelf(nums)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
