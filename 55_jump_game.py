'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''

class Solution:
    def canJump(self, nums):
        #只需要知道True 或 False

        #[2,3,1,1,4]

        maxPosition = 0
        nLen = len(nums)

        for i in range(nLen):
            if maxPosition < i:
                return False
            else:
                maxPosition = max(maxPosition, i + nums[i])
                if maxPosition >= nLen - 1:
                    return True

        return False



if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    result = sol.canJump(nums)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
