
'''
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        nLen = len(nums)
        
        for i in range(nLen-2):
            l = i + 1
            r = nLen - 1

            while l < r:
                val = nums[i] + nums[l] + nums[r]
                
                if val == target:
                    return val
                
                if abs(val - target) < abs(result - target):
                    result = val
                    
                if val > target:
                    r -= 1
                else:
                    l += 1
        
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1
    result = sol.threeSumClosest(nums, target)
    print(result)
    print('success')
    print('time complexity: O(n^2)')
    print('space complexity: O(1)')
