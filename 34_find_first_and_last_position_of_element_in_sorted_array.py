'''
Input: nums = [5,7,7,8,8,10], target = 8
                     lr
                     lr
                       lr
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1] 

Input: nums = [], target = 0
Output: [-1,-1]
'''

class Solution:
    def findFirstPosition(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = int(l + (r-l) / 2)

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                r = mid
            else:
                r = mid - 1

        return l if nums[l] == target else -1

    def findLastPosition(self, nums, start):
        target = nums[start]
        result = start
        for i in range(start, len(nums)):
            if nums[i] == target:
                result = i
            else:
                break
        return result

    def searchRange(self, nums, target):
        nLen = len(nums)

        if nLen == 0:
            return [-1, -1]
        
        firstPosition = self.findFirstPosition(nums, target)
        if firstPosition == -1:
            return [-1, -1]
        lastPosition = self.findLastPosition(nums, firstPosition)

        return [firstPosition, lastPosition]

if __name__ == '__main__':
    sol = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    result = sol.searchRange(nums, target)
    print(result)
    print('success')
    print('time complexity: O(log n)')
    print('space complexity: O(1)')
