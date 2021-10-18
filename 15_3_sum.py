'''
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSum(self, nums):
        #sort
        #for loop + two pointer
        nums.sort()
        result = []
        nLen = len(nums)
        for i in range(nLen-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = nLen - 1
            
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                
                if val == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1
        return result
        
        


if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    result = sol.threeSum(nums)
    print(result)
    print('success')
    print('time complexity: O(n^2)')
    print('space complexity: O(n)')
