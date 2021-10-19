'''
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

class Solution:
    def jump(self, nums):
        #dp initial max size
        #for record d[j]
        nLen = len(nums)
        dp =  [nLen for _ in range(nLen)]
        dp[0] = 0

        for i in range(nLen):
            step = nums[i]
            for j in range(i+1, min(i+step+1, nLen)):
                dp[j] = min(dp[j], dp[i] + 1)
                if j  == nLen - 1:
                    return dp[-1]
        return dp[-1]

if __name__ == '__main__':
      sol = Solution()
      nums = []
      result = sol.jump(nums)
      print(result)
      print('success')
      print('time complexity: O(n)')
      print('space complexity: O(n)')
